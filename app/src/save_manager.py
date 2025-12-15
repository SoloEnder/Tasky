
import json
import logging

logger = logging.getLogger(__name__)

def file_operation_exception(func):

    def wrapper(filepath, data=None):

        try:
            data = func(filepath, data)

        except FileNotFoundError:
            logger.warning(f"No file found at {filepath}")
            return
        
        except json.JSONDecodeError:
            logger.warning(f"Unable to load data from file {filepath} : file corrupted")
            return

        except PermissionError:
            logger.warning(f"Unable to load data from file {filepath} : permission denied")
            return

        except Exception as e:
            logger.warning(f"Unable to load data from file {filepath}\n{e}")
            return
        
        else:
            return data

    return wrapper

@file_operation_exception
def save_data(filepath: str, data):
    save_data.filepath = filepath

    with open(filepath, "w") as f:
        json.dump(data, f)

    logger.info(f"Data saved at {filepath}")

@file_operation_exception
def load_data(filepath: str, data):
    load_data.filepath = filepath

    with open(filepath, "r") as f:
        data = json.load(f)

    logger.info(f"Data loaded from {filepath}")
    return data
        