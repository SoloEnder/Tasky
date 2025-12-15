
import json
import logging
from app.utils.username_hidder import remove_username

logger = logging.getLogger(__name__)

def file_operation_exception(func):

    def wrapper(filepath, data=None):
        filepath_without_username = remove_username(filepath)

        try:
            data = func(filepath, data)

        except FileNotFoundError:
            logger.warning(f"No file found at {filepath_without_username}")
            return
        
        except json.JSONDecodeError:
            logger.warning(f"Unable to load data from file {filepath_without_username} : file corrupted")
            return

        except PermissionError:
            logger.warning(f"Unable to load data from file {filepath_without_username} : permission denied")
            return

        except Exception as e:
            logger.warning(f"Unable to load data from file {filepath_without_username}\n{e}")
            return
        
        else:
            return data

    return wrapper

@file_operation_exception
def save_data(filepath: str, data):
    save_data.filepath = filepath

    with open(filepath, "w") as f:
        json.dump(data, f)

    logger.info(f"Data saved at {remove_username(filepath)}")

@file_operation_exception
def load_data(filepath: str, data):
    load_data.filepath = filepath

    with open(filepath, "r") as f:
        data = json.load(f)

    logger.info(f"Data loaded from {remove_username(filepath)}")
    return data
        