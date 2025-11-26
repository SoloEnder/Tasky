
import customtkinter as ctk
from .tasks_screen.tasks_screen import TasksScreen

class SideBarFrame(ctk.CTkFrame):
    """
    An instance of customtkinter.CTkFrame, which handle all the screens of the app
    """

    def __init__(self, master, user, **kwargs):
        super().__init__(master, **kwargs)
        self.columnconfigure(0, weight=1)
        self.master = master
        self.buttons = {}
        
        index = 0

        for screen_name, screen_object in self.master.screens.items():  #type: ignore
            button = ctk.CTkButton(self, text=screen_name, height=35, font=("default", 15), command=lambda sn=list(self.master.screens.keys())[index]: self.master.switch_frame(sn)) #type: ignore
            button.grid(row=index, column=0, sticky="new", pady=10)
            self.buttons[screen_name] = button
            index += 1

        print(self.buttons)
