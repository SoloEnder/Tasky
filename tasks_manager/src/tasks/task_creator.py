
import logging
from tasks_manager.ui.tasks_screen.task_fr import TaskFrame

logger = logging.getLogger(__name__)

def create_task(master, task_data):
    logger.info("A task frame creation request has been received")
    return TaskFrame(master, task_data=task_data)
