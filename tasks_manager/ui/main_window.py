import logging 
import customtkinter as ctk
from app.tasky.utils import events_handlers
from app.tasky.ui.sidebar import SideBarFrame
from app.tasky.ui import settings_screen
from app.tasky.ui.tasks_screen import tasks_screen
from app.tasky.src.tasks.tasks_data_handler import tasks_data_handler
import logging

class MainWindow(ctk.CTk):
    """
    The windows

    Inherit from customtkinter.CTk
    """

    def __init__(self, master):
        self.master = master
        super().__init__()
        self.title("Tasks Manager")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.events_handler = events_handlers.main_events_handler

        #  Creating events
        self.events_infos = {
            "Tasky.Ui.ScreenSwitched":{"ancient_screen":None, "new_screen":None}, 
            "Tasky.Ui.ScreenAdded":{"screen":None}, 
            "Tasky.Ui.ScreenDeleted":{"screen_name":None},
            "Tasky.Ui.WindowsClosed":{},
            }
        
        for event_name, event_kw in self.events_infos.items():
            event = events_handlers.Event(name=event_name, **event_kw)
            self.events_handler.add_event(event)

        self.tasks_data_handler = tasks_data_handler
        self.tasks_data = self.tasks_data_handler.tasks_data
        self.logger = logging.getLogger(__name__)
        self.screens = {"Tasks":tasks_screen.TasksScreen(self), "Settings":settings_screen.SettingsScreen(self)}
        self.current_screen = ("Tasks", self.screens["Tasks"])
        self.side_bar = SideBarFrame(self)
        self.side_bar.grid(row=0, column=0, sticky="nsew")
        self.switch_frame("Tasks", destroy=False)

    def on_closing(self):
        self.logger.debug("Window closure request received")
        self.destroy()
        self.logger.info("Window closed")

    def switch_frame(self, frame_name: str, destroy: bool=False, ungrid_current: bool=True):
        ancient_screen_obj = self.current_screen[1]

        if ungrid_current:
            ancient_screen_obj.grid_forget()

        self.frame_object = self.screens[frame_name]
        self.logger.debug(f"Frame name : {frame_name}")
        self.logger.debug(f"Frame object : {self.frame_object}")

        if destroy:
            self.current_screen[1].destroy()

        self.current_screen = (frame_name, self.frame_object)
        self.current_screen[1].grid(row=0, column=1, sticky="nsew")
        self.logger.debug(f"Current screen : {self.frame_object}")
        self.events_handler.raise_event(
            "Tasky.Ui.ScreenSwitched", 
            ancient_screen=ancient_screen_obj, 
            new_screen=self.current_screen[1]
            )
        self.side_bar.refresh() 

    def add_screen(self, name: str, object):
        self.screens[name] = object
        self.events_handler.raise_event(
            "Tasky.Ui.ScreenAdded",
            screen=object,
            )
        self.side_bar.refresh() 

    def remove_screen(self, name: str):
        del self.screens[name]
        self.events_handler.raise_event(
            "Tasky.Ui.ScreenDeleted",
            screen_name=name,
            )
        self.side_bar.refresh() 
