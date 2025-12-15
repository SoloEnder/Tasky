
import logging
import logging.handlers

def username_formatter(self)

def set_logger(logger, logs_filepath: str):
    global_logger = logger
    global_logsfile_handler = logging.handlers.RotatingFileHandler(logs_filepath, maxBytes=10000, backupCount=3)
    global_logsfile_handler.setLevel("DEBUG")
    global_logs_formatter = logging.Formatter(fmt="[{asctime}] - [{name}] - [{levelname}] : {msg}", style="{")
    global_logsfile_handler.setFormatter(global_logs_formatter)
    global_logs_streamhandler = logging.StreamHandler()
    global_logs_streamhandler.setFormatter(global_logs_formatter)
    global_logs_streamhandler.setLevel(logging.DEBUG)
    global_logger.addHandler(global_logsfile_handler)
    global_logger.addHandler(global_logs_streamhandler)
    global_logger.setLevel(logging.DEBUG)