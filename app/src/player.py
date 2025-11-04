
import json
from tkinter.messagebox import showerror
import os
from tkinter.messagebox import showinfo
from .save_manager import save_data, load_data

class Player:

    def __init__(self, master, **kwargs) -> None:
        self.master = master
        self.name = kwargs.get("name", "Player")
        self.level = kwargs.get("level", 0)
        self.current_xp = kwargs.get("current_xp", 0)
        self.xp_for_level_up = kwargs.get("xp_for_level_up", 10)
        self.total_xp = kwargs.get("total_xp", 0)
        self.hp = kwargs.get("hp", 20)
        self.max_hp = kwargs.get("hp_max", 20)
        self.strength = kwargs.get("strength", 5)
        self.max_strength = kwargs.get("max_strength", 5)
        self.defense = kwargs.get("defense", 2)
        self.max_defense = kwargs.get("max_defense", 2)
        self.backupdir_path =  os.path.join(os.getenv("APPDATA", os.path.join(os.path.expanduser("~"), "AppData/Roaming/Tasks Gamifier")), "Tasks Gamifier")

        self.backupfilename = "player_infos.json"
        self.backupfile_path = os.path.join(self.backupdir_path, self.backupfilename)

    def save_data(self):
        """
        Save the player data in a file
        """
        print("Saving player data...")

        data = {
            "name":self.name, 
            "level":self.level,
            "current_xp":self.current_xp,
            "xp_for_level_up":self.xp_for_level_up,
            "total_xp": self.total_xp,
            "hp":self.hp,
            "max_hp":self.max_hp, 
            "strength":self.strength,
            "max_strength": self.max_strength,
            "defense":self.defense,
            "max_defense": self.max_defense,
            }
        save_data(self.backupfile_path, data)

    def load_data(self):
        print("Loading player infos backup file...")
        data = load_data(self.backupfile_path)

        if data:
            self.name = data["name"]
            self.level = data["level"]
            self.current_xp = data["current_xp"]
            self.xp_for_level_up = data["xp_for_level_up"]
            self.total_xp = data["total_xp"]
            self.hp = data["hp"]
            self.max_hp = data["max_hp"]
            self.strength = data["strength"]
            self.max_strength = data["max_strength"]
            self.defense = data["defense"]
            self.max_defense = data["max_defense"]


    def add_xp(self, amount, add_to_total: bool = True):

        if add_to_total:
            self.total_xp += amount

        if self.current_xp >= self.xp_for_level_up:
            diff = self.xp_for_level_up - self.current_xp
            self.current_xp = 0
            self.xp_for_level_up += 10
            self.level += 1
            showinfo("Tasks Gamifier | Level up ", message="You have level up !")
            self.add_xp(abs(diff), add_to_total=False)

        else:
            self.current_xp += amount

