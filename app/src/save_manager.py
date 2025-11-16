
import json
import logging
from app.utils.username_hidder import remove_username

logger = logging.getLogger(__name__)

def save_data(filepath: str, data):


    with open(filepath, "w") as f:
        json.dump(data, f)

    logger.info(f"Data saved at {remove_username(filepath)}")

def load_data(filepath: str):
    filepath_without_username = remove_username(filepath)

    try:

        with open(filepath, "r") as f:
            data = json.load(f)

    except FileNotFoundError:
        logger.info(f"No file found at {filepath_without_username}")
        return
    
    except json.JSONDecodeError:
        logger.info(f"Unable to load data from file {filepath_without_username} : file corrupted")
        return

    except PermissionError:
        logger.info(f"Unable to load data from file {filepath_without_username} : permission denied")
        return

    except Exception as e:
        logger.info(f"Unable to load data from file {filepath_without_username}\n{e}")
        return

    else:
        logger.info(f"Data loaded from {remove_username(filepath)}")
        return data
        