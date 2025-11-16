
import logging
import logging.handlers
from app.utils import paths

logger = logging.getLogger()
logsfile_handler = logging.handlers.RotatingFileHandler(paths.logs_basefile, maxBytes=1000000, backupCount=3)
logsfile_handler.setLevel("DEBUG")
logs_formatter = logging.Formatter(fmt="[{asctime}] - [{name}] - [{levelname}] : {msg}", style="{")
logsfile_handler.setFormatter(logs_formatter)
logs_streamhandler = logging.StreamHandler()
logs_streamhandler.setFormatter(logs_formatter)
logs_streamhandler.setLevel(logging.CRITICAL)
logger.addHandler(logsfile_handler)
logger.addHandler(logs_streamhandler)
logger.setLevel("DEBUG")