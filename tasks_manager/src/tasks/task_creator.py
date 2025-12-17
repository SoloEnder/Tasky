
import logging
from tasks_manager.ui.tasks_screen.task_fr import TaskFrame

logger = logging.getLogger(__name__)

def create_task(master, task_data):
    return TaskFrame(master, task_data=task_data)
