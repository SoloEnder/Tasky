
import logging

class TasksManagerApp:

    def __init__(self, master=None):
        self.master = master
        self.logger = logging.getLogger("tasks_manager")