
import os
import logging, logging.handlers
from app import tasky
from app import tasky_dungeon
from app
from app.boot import check_and_make 
from app.utils import paths
from app.utils import events_handlers

class App:

    def __init__(self):
        check_and_make("program_dir", "logs_dir")
        self.set_logger()
        check_and_make("data_dir", "user_data_dir")
        self.logger = logging.getLogger(__name__)
        self.events_handler = events_handlers.main_events_handler
        self.tasky = tasky
        self.tasky_dungeon = tasky_dungeon
        self.tasky_window = self.tasky.ui.MainWindow(self)

    def running(self):
        self.auto_save()
        self.logger.info("Main window drawed")
        self.exit_app()

    def exit_app(self):
        self.logger.info("Saving data...")
        self.logger.info("Exit folowing main window closure")
        exit()

    def auto_save(self):
        self.logger.info("Auto saving...")
        self.tasky_window.after(120000, self.auto_save)

    def set_logger(self):
        global_logger = logging.getLogger("app")
        global_logsfile_handler = logging.handlers.RotatingFileHandler(paths.logs_basefile, maxBytes=10000, backupCount=3)
        global_logsfile_handler.setLevel("DEBUG")
        global_logs_formatter = logging.Formatter(fmt="[{asctime}] - [{name}] - [{levelname}] : {msg}", style="{")
        global_logsfile_handler.setFormatter(global_logs_formatter)
        global_logs_streamhandler = logging.StreamHandler()
        global_logs_streamhandler.setFormatter(global_logs_formatter)
        global_logs_streamhandler.setLevel(logging.DEBUG)
        global_logger.addHandler(global_logsfile_handler)
        global_logger.setLevel(logging.DEBUG)


