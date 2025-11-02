import logging 
import customtkinter as ctk
from .tabview import TabView
from ..src.tasks.tasks_data_handler import tasks_data_handler

class App(ctk.CTk):
    """
    The windows

    Inherit from customtkinter.CTk
    """

    def __init__(self):
        super().__init__()
        self.title("Tasks Gamifier")
        self.geometry("500x440")
        self.resizable(False, False)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.tasks_data_handler = tasks_data_handler
        self.tasks_data_handler.load_tasks_data()
        self.tasks_data = self.tasks_data_handler.tasks_data
        self.tabview = TabView(self)
        self.tabview.grid(sticky="nsew")

    def on_closing(self):
        self.tasks_data_handler.save_tasks_data()
        self.destroy()

