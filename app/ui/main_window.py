import logging 
import customtkinter as ctk
from .tabview import TabView
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
        self.resizable(False, False)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.protocol("WM_DELETE_WINDOW")
        self.tasks_data_handler = tasks_data_handler
        self.tasks_data_handler.load_tasks_data()
        self.tasks_data = self.tasks_data_handler.tasks_data
        self.tabview = TabView(self, user)
        self.tabview.grid(sticky="nsew")
        self.logger = logging.getLogger(__name__)


