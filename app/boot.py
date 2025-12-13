
import os
import logging
from app.tasky.utils import paths
from app.tasky.utils.username_hidder import remove_username

logger = logging.getLogger(__name__)

existing_paths_alias = {
    "program_dir":paths.base_path,
    "data_dir":paths.data_dir,
    "logs_dir":paths.logs_dir,
    "user_data_dir":paths.user_data_dir,
}

def check_and_make(*paths_alias):
    """
    Check the existence of a path alias in the path database of the program. Create it if the path is found in the database, but don't exists

    Args:
        - path_name (str): a alias of a path. See the attribute 'paths_list' for see paths alias

    """

    for alias in paths_alias:

        if not alias in existing_paths_alias:
            logger.warning("Unable to found path alias for given alias '{alias}'")
            raise ValueError(f"No path found for given alias '{alias}'")

        else:
            path = existing_paths_alias[alias]
            path_without_username = remove_username(path)
            logger.info(f"Checking the existence of {path_without_username}...")

        if not os.path.exists(path):
            logger.warning(f"Folder at {path_without_username} not found, attempting to make it...")

            try:
                os.mkdir(path)

            except Exception as e:
                logger.warning(f"Failed to create folder at {path_without_username}\n[...] : {e}")

            else:
                logger.info(f"Folder {path_without_username} created")

