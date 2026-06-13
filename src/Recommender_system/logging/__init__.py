import os
import sys
import logging

# A single, consistently-formatted logger for the whole project.
# Modules use it via:  from src.Recommender_system.logging import logger
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "logging.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),   # persist logs to logs/logging.log
        logging.StreamHandler(sys.stdout),   # and echo to the console
    ],
)

logger = logging.getLogger("recommender_logger")
