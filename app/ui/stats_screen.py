import customtkinter as ctk

class StatsScreen(ctk.CTkFrame):
    """
    An instance of customtkinter.CTkFrame that contains all the widgets for managing and displaying user statistics
    """

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        #Player stats widgets
        self.player_name_font = ctk.CTkFont(weight="bold", size=22)
        self.stat_title_font = ctk.CTkFont(weight="bold", size=16)

        self.player_name_lb = ctk.CTkLabel(self, text="Player", font=self.player_name_font)
        self.player_name_lb.grid(row=0, sticky="w")

        self.lvl_value = ctk.CTkLabel(self, text="(Lv.0)")
        self.lvl_value.grid(row=0, sticky="e")

        self.xp_value_pb = ctk.CTkProgressBar(self, height=12)
        self.xp_value_pb.grid(row=0, column=1, sticky="e")
        self.xp_value_pb.set(0)

        self.hp_name_lb = ctk.CTkLabel(self, text="Health", font=self.stat_title_font)
        self.hp_name_lb.grid(row=1, column=0, sticky="w")
        self.hp_value_lb = ctk.CTkLabel(self, text="0/0")
        self.hp_value_lb.grid(row=1, column=0, sticky="e")
        self.hp_value_pb = ctk.CTkProgressBar(self, height=12)
        self.hp_value_pb.set(0)
        self.hp_value_pb.grid(row=1, column=1, sticky="e")

        self.stats_infos = [("Strength", "0"), ("Defense", "0")]

        for index, stat_infos in enumerate(self.stats_infos):
            self.stat_name_lb = ctk.CTkLabel(self, text=stat_infos[0], font=self.stat_title_font)
            self.stat_name_lb.grid(row=index+2, column=0, sticky="w")
            self.stat_value_lb = ctk.CTkLabel(self, text=stat_infos[1])
            self.stat_value_lb.grid(row=index+2, column=1, sticky="e")

    def update_stat_value(self, stat_value_widget, new_value: str|float|int, is_progressbar: bool=False):
        """
        Updates the 'text' value of a customtkinter widget to a new value, or changes the value of a customtkinter progress bar

        Args:
            - stat_value_widget : a customtkinter widget with a 'text' attribute or a customtkinter.Progressbar object
            - new_value (str, int, float): the new value to pass to the widget
            - is_progressbar (bool): indicates whether the widget is a progress bar. default to 'False'
        """

        if not is_progressbar:
            stat_value_widget.configure(text=new_value)

        else:
            stat_value_widget.set(new_value)

