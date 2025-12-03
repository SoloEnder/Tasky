
import customtkinter as ctk

class Screen(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.widgets = {}