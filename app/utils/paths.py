import os
from pathlib import Path
import platform

system = platform.system()

# ------------------------------
# Base directory depending on OS
# ------------------------------
if system == "Windows":
    # Exemple : C:\Users\Name\AppData\Roaming\Tasky
    base_path = Path(os.getenv("APPDATA")) / "Tasky"
elif system == "Darwin":
    # macOS : ~/Library/Application Support/Tasky
    base_path = Path.home() / "Library" / "Application Support" / "Tasky"
else:
    # Linux : ~/.local/share/Tasky
    base_path = Path.home() / ".local" / "share" / "Tasky"

# ------------------------------
# Subdirectories
# ------------------------------
data_dir = base_path / "data"
user_data_dir = data_dir / "user"
logs_dir = base_path / "logs"

# ------------------------------
# Create folders if missing
# ------------------------------
for folder in (data_dir, user_data_dir, logs_dir):
    folder.mkdir(parents=True, exist_ok=True)

# ------------------------------
# Files
# ------------------------------
tasks_backup_file = user_data_dir / "tasks.json"
logs_basefile = logs_dir / "app.log"
