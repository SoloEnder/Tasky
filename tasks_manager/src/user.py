

class User:

    def __init__(self, master, **kwargs) -> None:
        self.master = master
        self.dev_mode =  True
        self.completed_tasks = []
