
import customtkinter as ctk

class Screen(ctk.CTkFrame):

    def __init__(self, master, name, **kwargs):
        super().__init__(self, **kwargs)
        self.name = name