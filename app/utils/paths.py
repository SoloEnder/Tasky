
import os
import __main__

# Quand le code est compilé via PyInstaller, os.path.dirname(__main__.__file__) renvoit chemin_quelconque\Tasky\_internal
isforwindows = False
base_path = os.path.dirname(__main__.__file__) if not isforwindows else os.path.dirname(os.path.dirname(__main__.__file__))
data_dir = os.path.join(base_path, "data") # Data folder

user_data_dir = os.path.join(data_dir, "user") # User data directory

RESS_DIR = os.path.join(base_path, "ress") # This directory contains ressources for the app

ASSETS_DIR = os.path.join(RESS_DIR, "assets") # Assets directory
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")
ICONS_FONT_FILEPATH = os.path.join(FONTS_DIR, "icons.ttf")


tasks_backup_file = os.path.join(user_data_dir, "tasks.json") # Tasks backup file 

logs_dir = os.path.join(base_path, "logs")
app_logsfile = os.path.join(logs_dir, "app.log")
tasks_manager_logsdir = os.path.join(logs_dir, "tasks_manager")
tasks_manager_logsfile = os.path.join(tasks_manager_logsdir, "tasks_manager.log")
tasky_dungeon_logsdir = os.path.join(logs_dir, "tasky_dungeon")
tasky_dungeon_logsfile = os.path.join(tasky_dungeon_logsdir, "tasky_dungeon.log")