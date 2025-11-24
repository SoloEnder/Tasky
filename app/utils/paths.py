
import os
import __main__

# Quand le code est compilé via PyInstaller, os.path.dirname(__main__.__file__) renvoit chemin_quelconque\Tasky\_internal
isforwindows = False
base_path = os.path.dirname(__main__.__file__) if not isforwindows else os.path.dirname(os.path.dirname(__main__.__file__))
data_dir = os.path.join(base_path, "data") # Data folder

user_data_dir = os.path.join(data_dir, "user") # User data directory
tasks_backup_file = os.path.join(user_data_dir, "tasks.json") # Tasks backup file 

logs_dir = os.path.join(base_path, "logs")
logs_basefile = os.path.join(logs_dir, "app.log")