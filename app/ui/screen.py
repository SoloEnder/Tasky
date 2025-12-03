
import customtkinter as ctk

class Screen(ctk.CTkFrame or ctk.CTkToplevel):

    def __init__(self, master, **kwargs):
        """
        The mother model class for the screens classes
        """
        super().__init__(master, **kwargs) # master est une instance d'une classe container de customtkinter ou de tkinter
        self.widgets = {}