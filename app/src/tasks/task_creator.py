
from ...ui.tasks_screen.task_fr import TaskFrame

def create_task(master, player, task_data):
    return TaskFrame(master, task_data=task_data, player=player)
