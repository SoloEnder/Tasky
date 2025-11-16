
import os
from app.ui.main_window import MainWindow
from app.src.tasks.tasks_data_handler import tasks_data_handler
from app.src.user import User
from app.src  import save_manager
import logging, logging.handlers
from app.src.boot import check_and_make 
from app.utils import paths

class App:

    def __init__(self):
        self.user = User(self)
        check_and_make("program_dir", "logs_dir")
        self.set_logger()
        check_and_make("data_dir", "user_data_dir")
        self.logger = logging.getLogger(__name__)
        self.tasks_data_handler = tasks_data_handler
        self.tasks_data_handler.load_tasks_data()
        self.main_window = MainWindow(self, self.user)


    def running(self):
        self.auto_save()
        self.logger.info("Main window drawed")
        self.main_window.mainloop()
        self.exit_app()

    def exit_app(self):
        self.logger.info("Saving data...")
        self.tasks_data_handler.save_tasks_data()
        self.logger.info("Exit folowing main window closure")
        exit()

    def auto_save(self):
        self.logger.info("Auto saving...")
        self.tasks_data_handler.save_tasks_data()
        self.main_window.after(120000, self.auto_save)

    def set_logger(self):
        global_logger = logging.getLogger("app")
        global_logsfile_handler = logging.handlers.RotatingFileHandler(paths.logs_basefile, maxBytes=1000000, backupCount=3)
        global_logsfile_handler.setLevel("DEBUG")
        global_logs_formatter = logging.Formatter(fmt="[{asctime}] - [{name}] - [{levelname}] : {msg}", style="{")
        global_logsfile_handler.setFormatter(global_logs_formatter)
        global_logs_streamhandler = logging.StreamHandler()
        global_logs_streamhandler.setFormatter(global_logs_formatter)
        global_logs_streamhandler.setLevel(logging.CRITICAL)
        global_logger.addHandler(global_logsfile_handler)
        global_logger.setLevel(logging.DEBUG)


