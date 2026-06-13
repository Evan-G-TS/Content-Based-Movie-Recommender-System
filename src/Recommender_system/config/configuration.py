from src.Recommender_system.constants import *
from src.Recommender_system.utils.common import read_yaml, create_directories
from src.Recommender_system.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    """Central hub that loads the YAML config files and hands out
    strongly-typed config objects for each pipeline stage."""

    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH,
                 schema_filepath=SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_table=config.source_table,
            local_data_file=config.local_data_file,
            batch_size=config.batch_size,
        )
        return data_ingestion_config
