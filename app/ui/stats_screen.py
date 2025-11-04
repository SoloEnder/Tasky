import customtkinter as ctk

class StatsScreen(ctk.CTkFrame):
    """
    An instance of customtkinter.CTkFrame that contains all the widgets for managing and displaying user statistics
    """

    def __init__(self, master, player, **kwargs):
        super().__init__(master, **kwargs)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.player = player

        #Player stats widgets

        self.name_sv = ctk.StringVar(self)
        self.lvl_sv = ctk.StringVar(self)
        self.stats_widgets = {}

        # Fonts
        self.stat_value_font = ctk.CTkFont(size=15)
        self.player_name_font = ctk.CTkFont(weight="bold", size=22)
        self.stat_title_font = ctk.CTkFont(weight="bold", size=16)

        self.player_name_lb = ctk.CTkLabel(self, text="Player", font=self.player_name_font)
        self.player_name_lb.grid(row=0, sticky="w")

        self.lvl_value = ctk.CTkLabel(self, text="(Lv.0)")
        self.lvl_value.grid(row=0, column=1, sticky="e")

        self.xp_name_lb = ctk.CTkLabel(self, text="XP", font=self.stat_title_font).grid(row=1, column=0, sticky="w")
        self.xp_value_lb = ctk.CTkLabel(self, text="0/0", font=self.stat_value_font)
        self.xp_value_lb.grid(row=1, column=0, sticky="e")
        self.xp_value_pb = ctk.CTkProgressBar(self, height=12, progress_color="yellow")
        self.xp_value_pb.grid(row=1, column=1, sticky="e")
        self.xp_value_pb.set(0)

        self.hp_name_lb = ctk.CTkLabel(self, text="Health", font=self.stat_title_font)
        self.hp_name_lb.grid(row=2, column=0, sticky="w")
        self.hp_value_lb = ctk.CTkLabel(self, text="0/0", font=self.stat_value_font)
        self.hp_value_lb.grid(row=2, column=0, sticky="e")
        self.hp_value_pb = ctk.CTkProgressBar(self, height=12, progress_color="red")
        self.hp_value_pb.set(0)
        self.hp_value_pb.grid(row=2, column=1, sticky="e")

        self.stats_infos = [("Strength", "0"), ("Defense", "0")]

        for index, stat_infos in enumerate(self.stats_infos):
            self.stat_name_lb = ctk.CTkLabel(self, text=stat_infos[0], font=self.stat_title_font)
            self.stat_name_lb.grid(row=index+3, column=0, sticky="w")
            self.stat_value_lb = ctk.CTkLabel(self, text=stat_infos[1], font=self.stat_value_font)
            self.stat_value_lb.grid(row=index+3, column=1, sticky="e")
            self.stats_widgets[stat_infos[0]] = self.stat_value_lb

        self.auto_update()

    def auto_update(self):
        self.player_name_lb.configure(text=f"{self.player.name}")
        self.hp_value_lb.configure(text=f"{self.player.hp}/{self.player.max_hp}")
        self.hp_value_pb.set(self.player.max_hp/self.player.hp)
        self.lvl_value.configure(text=f"Lv.{self.player.level}")
        self.xp_value_lb.configure(text=f"{self.player.current_xp}/{self.player.xp_for_level_up}")
        self.xp_value_pb.set(self.player.current_xp/self.player.xp_for_level_up)
        self.stats_widgets["Strength"].configure(text=f"{self.player.strength}/{self.player.max_strength}")
        self.stats_widgets["Defense"].configure(text=f"{self.player.defense}/{self.player.max_defense}")
        self.after(800, self.auto_update)

