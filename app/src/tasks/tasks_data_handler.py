
import json
from ...src.save_manager import save_data, load_data
import os

class TasksDataHandler():

    def __init__(self, tasks_data: list=[]):
        self.tasks_data = tasks_data
        self.backupdir_path =  os.path.join(os.getenv("APPDATA", os.path.join(os.path.expanduser("~"), "AppData/Roaming/Tasks Gamifier")), "Tasks Gamifier")

        if not os.path.exists(self.backupdir_path):
            print("No backup folder found !")
            print("Creating backup folder...")
            os.mkdir(self.backupdir_path)

        self.backupfilename = "tasks.json"
        self.backupfile_path = os.path.join(self.backupdir_path, self.backupfilename)

    def save_tasks_data(self):
        print("Saving tasks data...")
        save_data(self.backupfile_path, self.tasks_data)
       

    def load_tasks_data(self):
        print("Loading tasks backup file...")
        self.tasks_data = load_data(self.backupfile_path)

        if not self.tasks_data:
            self.tasks_data = []

        
tasks_data_handler = TasksDataHandler()

