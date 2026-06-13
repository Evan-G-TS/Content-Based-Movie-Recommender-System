from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    """Settings for the Data Ingestion stage.

    Pulls the db1-rich `movies` table from Supabase and lands it, raw, as a CSV.
    No filtering happens here — that belongs to Data Transformation (Bucket 3).
    Credentials are read from the .env file by the component, never stored here.
    """
    root_dir: Path
    source_table: str
    local_data_file: Path
    batch_size: int
