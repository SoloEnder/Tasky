
import customtkinter as ctk
from .stats_screen import StatsScreen
from .tasks_screen.tasks_screen import TasksScreen

class TabView(ctk.CTkTabview):
    """
    An instance of customtkinter.CTkTabView, which handle all the screens of the app
    """

    def __init__(self, master, player, **kwargs):
        super().__init__(master, **kwargs)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.master = master

        self.tasks_tab = self.add("Tasks")
        self.tasks_screen = TasksScreen(
            self.tasks_tab,
            player,
            )
        self.tasks_tab.rowconfigure(0, weight=1)
        self.tasks_tab.columnconfigure(0, weight=1)
        self.tasks_screen.grid(sticky="nsew")
        
        self.stats_tab = self.add("Stats")
        self.stats_screen = StatsScreen(
            self.stats_tab,
            player,
            )
        self.stats_tab.rowconfigure(0, weight=1)
        self.stats_tab.columnconfigure(0, weight=1)
        self.stats_screen.grid(sticky="nsew")


