
import logging
import logging.handlers
import os

class SensitiveInfoFilter(logging.Filter):

    def filter(self, record):
        userpath = os.path.expanduser("~")

        if userpath.lower() in record.getMessage().lower():
            record.msg = record.getMessage().replace(userpath, "USERDIR")
            record.args = ()
        return True


def set_logger(logger, logs_filepath: str):
    global_logger = logger
    global_logsfile_handler = logging.handlers.RotatingFileHandler(logs_filepath, maxBytes=10000, backupCount=3)
    global_logsfile_handler.setLevel(logging.INFO)
    global_logs_formatter = logging.Formatter(fmt="[{asctime}] - [{name}] - [{levelname}] : {msg}", style="{")
    global_logsfile_handler.setFormatter(global_logs_formatter)
    global_logs_streamhandler = logging.StreamHandler()
    global_logs_streamhandler.setFormatter(global_logs_formatter)
    global_logs_streamhandler.setLevel(logging.DEBUG)
    global_logger.addHandler(global_logsfile_handler)
    global_logger.addHandler(global_logs_streamhandler)
    global_logger.setLevel(logging.DEBUG)
    global_logs_streamhandler.addFilter(SensitiveInfoFilter())