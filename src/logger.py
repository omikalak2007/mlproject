import logging
import os
from datetime import datetime

# Define the log file name and directory path
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir = os.path.join(os.getcwd(), "logs")  # Directory path for logs
os.makedirs(log_dir, exist_ok=True)  # Create the directory if it doesn't exist

LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)  # Full path to the log file

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s ",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")
