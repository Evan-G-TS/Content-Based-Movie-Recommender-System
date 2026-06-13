import os

import pandas as pd
import psycopg2
from dotenv import load_dotenv

from src.Recommender_system.logging import logger
from src.Recommender_system.entity.config_entity import DataIngestionConfig


class DataIngestion:
    """Data Ingestion component.

    Connects to the Supabase Postgres database, reads the configured source
    table in full, and writes it verbatim to a local CSV in the artifacts
    directory. This is the 'raw landing' step — no cleaning or filtering.
    """

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def _connect(self):
        """Open a psycopg2 connection using the credentials in .env.

        Mirrors the connection used in ping_to_supabase.ipynb
        (Supabase transaction pooler).
        """
        load_dotenv()  # SUPABASE Postgres creds: user / password / host / port / dbname
        return psycopg2.connect(
            user=os.getenv("user"),
            password=os.getenv("password"),
            host=os.getenv("host"),
            port=os.getenv("port"),
            dbname=os.getenv("dbname"),
            connect_timeout=30,
        )

    def fetch_from_supabase(self):
        """Read the source table from Supabase and save it as a raw CSV.

        The table is pulled in batches (ORDER BY ctid + LIMIT/OFFSET). A single
        SELECT of all ~85k rich rows overruns the Supabase transaction-pooler
        statement timeout, so we page through it with a fresh connection per
        batch — each query is short and reliable.

        Idempotent: if the raw file already exists we skip the network pull,
        so re-running the pipeline is cheap.
        """
        if os.path.exists(self.config.local_data_file):
            logger.info(
                f"Raw data already present at {self.config.local_data_file} — skipping Supabase fetch."
            )
            return

        table = self.config.source_table
        batch_size = self.config.batch_size
        logger.info(f"Connecting to Supabase and reading table '{table}' in batches of {batch_size:,} ...")

        frames = []
        columns = None
        offset = 0
        while True:
            conn = self._connect()
            try:
                cur = conn.cursor()
                # ORDER BY ctid gives a stable, unique ordering for safe pagination.
                cur.execute(
                    f'SELECT * FROM public."{table}" ORDER BY ctid LIMIT %s OFFSET %s;',
                    (batch_size, offset),
                )
                columns = [desc[0] for desc in cur.description]
                rows = cur.fetchall()
                cur.close()
            finally:
                conn.close()

            if not rows:
                break

            frames.append(pd.DataFrame(rows, columns=columns))
            offset += len(rows)
            logger.info(f"  fetched {offset:,} rows so far ...")

            if len(rows) < batch_size:
                break

        df = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame(columns=columns)
        df.to_csv(self.config.local_data_file, index=False)
        logger.info(
            f"Ingested {len(df):,} rows x {df.shape[1]} columns from '{table}' "
            f"-> {self.config.local_data_file}"
        )
