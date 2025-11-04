
from ..ui.main_window import MainWindow
from .player import Player

class App:

    def __init__(self):
        self.player = Player(self)
        self.player.load_data()
        self.main_window = MainWindow(self, self.player)

    def running(self):
        self.main_window.mainloop()
        self.exit_app()

    def exit_app(self):
        print("Saving data...")
        self.player.save_data()
        print("Closing main window...")

    def auto_save(self):
        print("Saving data...")
        self.player.save_data()
        self.main_window.tasks_data_handler.save_tasks_data()
        self.main_window.after(300000, self.auto_save)
