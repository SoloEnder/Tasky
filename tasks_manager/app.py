
import logging

from app.utils import logger_config
from app.utils import paths
from app.utils import existence_checker
from tasks_manager.ui import ui
from tasks_manager.src.tasks.tasks_data_handler import tasks_data_handler

class TasksManagerApp:

    def __init__(self, master=None):
        self.master = master
        existence_checker.existing_paths_alias["tasks_manager_logs_dir"] = paths.tasks_manager_logsdir
        existence_checker.check_and_make("tasks_manager_logs_dir")
        self.logger = logging.getLogger("tasks_manager")
        logger_config.set_logger(self.logger, paths.tasks_manager_logsfile)
        self.tasks_data_handler = tasks_data_handler
        self.tasks_data_handler.load_tasks_data()
        self.ui = ui.UI(self)
        self.ui.protocol("WM_DELETE_WINDOW", self.on_closing)

    def running(self):
        self.logger.info("Running...")
        self.ui.mainloop()

    def on_closing(self):
        self.logger.info("Closing main window...")
        self.ui.destroy()
        self.logger.info("Saving tasks data...")
        self.tasks_data_handler.save_tasks_data()
