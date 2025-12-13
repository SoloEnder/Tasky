
import json
import logging
from app.tasky.src.save_manager import save_data, load_data
from app.tasky.utils import paths

class TasksDataHandler():

    def __init__(self, tasks_data: list=[]):
        self.logger = logging.getLogger(__name__)
        self.tasks_data = tasks_data
        self.tasks_backup_filepath = paths.tasks_backup_file

    def save_tasks_data(self):
        save_data(self.tasks_backup_filepath, self.tasks_data)
        self.logger.info("Tasks data saved")
       

    def load_tasks_data(self):
        self.tasks_data = load_data(self.tasks_backup_filepath)

        if not self.tasks_data:
            self.tasks_data = []
            self.logger.warning("No task data found, creating empty task data list")

        else:
            self.logger.info("Tasks data loaded")

        
tasks_data_handler = TasksDataHandler()

