
import customtkinter as ctk
from app.src import player as player_module
import logging

class StatsScreen(ctk.CTkFrame):

    def __init__(self, master, player=None):
        super().__init__(master)
        self.columnconfigure((0, 1), weight=1)
        self.logger = logging.getLogger(__name__)
        self.player = player if player else player_module.Player("Player")

        self.widgets = {"labels":{}, "buttons":{}, "progress_bars":{}}
        self.stats = {"HP":{"current":self.player.hp, "max":self.player.max_hp}, "XP":{"current":self.player.xp, "max":self.player.xp_for_levelup}, "Strength":{"current":self.player.strength, "max":self.player.max_strength}, "Defense":{"current":self.player.defense, "max":self.player.max_defense}}

        # Text style
        self.header_style = ctk.CTkFont(weight="bold", size=22)
        self.stat_name_style = ctk.CTkFont(weight="bold", size=20)
        self.stat_value_style = ctk.CTkFont(size=18)

        # Widgets
        self.player_name_lb = ctk.CTkLabel(self, text=f"{self.player.name}", font=self.header_style)
        self.player_name_lb.grid(row=0, column=0, sticky="w", padx=15)
        self.player_lvl_lb = ctk.CTkLabel(self, text=f"(Lvl.{self.player.level})", font=self.header_style)
        self.player_lvl_lb.grid(row=0, column=0, sticky="e")
        self.widgets["labels"]["player_name"] = self.player_name_lb
        self.widgets["labels"]["player_lvl"] = self.player_lvl_lb

        self.widgets["labels"]["stats_names"] = {}
        self.widgets["labels"]["stats_values"] = {}
        stats_widgets_row = 1

        for stat_name, stat_values in self.stats.items():
            self.logger.debug(f"Stat name : {stat_name}")
            self.logger.debug(f"Stat value : {stat_values}")
            stat_name_lb = ctk.CTkLabel(self, text=stat_name, font=self.stat_name_style)

            if stat_name == "HP" or stat_name == "XP":
                stat_value_pb = ctk.CTkProgressBar(self, height=20, progress_color="red" if stat_name == "HP" else "yellow")
                stat_value_pb.set(stat_values["current"]/stat_values["max"])
                stat_value_pb.grid(row=stats_widgets_row, column=1, sticky="e", padx=15)
                self.widgets["progress_bars"][stat_name] = stat_value_pb

            else:
                stat_value_lb = ctk.CTkLabel(self, text=f"{stat_values["current"]}/{stat_values["max"]}", font=self.stat_value_style)
                stat_value_lb.grid(row=stats_widgets_row, column=1, sticky="e", padx=15)
                self.widgets["labels"]["stats_values"] = stat_value_lb

            stat_name_lb.grid(row=stats_widgets_row, column=0, sticky="w", pady=10, padx=15)
            self.widgets["labels"]["stats_names"] = stat_name_lb
            stats_widgets_row += 1



        