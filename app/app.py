
import os
import logging
import logging.handlers

from tasks_manager import app as tasks_manager_app
from app.utils.existence_checker import check_and_make
from app.utils import paths
from app.utils import logger_config
from app.utils import events_handlers

class App:

    def __init__(self):
        check_and_make("logs_dir")
        self.logger = logging.getLogger("app")
        logger_config.set_logger(self.logger, paths.app_logsfile)
        check_and_make("data_dir", "user_data_dir")
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setLevel(logging.DEBUG)
        self.logger.addHandler(self.stream_handler)
        self.events_handler = events_handlers.main_events_handler
        self.tasky = tasks_manager_app.TasksManagerApp(self)

    def running(self):
        self.tasky.running()
        self.exit_app()

    def exit_app(self):
        exit()
