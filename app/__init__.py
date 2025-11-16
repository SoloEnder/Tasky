
import logging
import logging.handlers
from app.utils import paths

logger = logging.getLogger()
logsfile_handler = logging.handlers.RotatingFileHandler(paths.logs_basefile, maxBytes=1000000, backupCount=3)
logsfile_handler.setLevel("DEBUG")
logs_formatter = logging.Formatter(fmt="[{asctime}] - [{name}] - [{levelname}] : {msg}", style="{")
logsfile_handler.setFormatter(logs_formatter)
logger.addHandler(logsfile_handler)
logger.setLevel("DEBUG")