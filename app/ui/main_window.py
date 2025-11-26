import logging 
import customtkinter as ctk
from .sidebar import SideBarFrame
from .settings_screen import settings_screen
from .stats_screen import stats_screen
from app.ui.tasks_screen import tasks_screen
from ..src.tasks.tasks_data_handler import tasks_data_handler
import logging

class MainWindow(ctk.CTk):
    """
    The windows

    Inherit from customtkinter.CTk
    """

    def __init__(self, master, user):
        self.master = master
        super().__init__()
        self.title("Tasks Manager")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.user = user
        self.tasks_data_handler = tasks_data_handler
        self.tasks_data = self.tasks_data_handler.tasks_data
        self.logger = logging.getLogger(__name__)
        self.screens = {"Tasks":tasks_screen.TasksScreen(self, self.user), "Settings":settings_screen.SettingsScreen(self), "Stats":stats_screen.StatsScreen(self)}
        self.current_screen = ("Tasks", self.screens["Tasks"])
        self.side_bar = SideBarFrame(self, user)
        self.side_bar.grid(row=0, column=0, sticky="nsew")
        self.switch_frame("Tasks", destroy=False)

    def on_closing(self):
        self.logger.debug("Window closure request received")
        self.destroy()
        self.logger.info("Window closed")

    def switch_frame(self, frame_name: str, destroy: bool=False, ungrid_current: bool=True):

        if ungrid_current:
            self.current_screen[1].grid_forget()

        self.frame_object = self.screens[frame_name]
        self.logger.debug(f"Frame name : {frame_name}")
        self.logger.debug(f"Frame object : {self.frame_object}")

        if destroy:
            self.current_screen[1].destroy()

        self.current_screen = (frame_name, self.frame_object)
        self.current_screen[1].grid(row=0, column=1, sticky="nsew")
        self.logger.debug(f"Current screen : {self.frame_object}")



