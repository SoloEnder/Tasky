
from app.utils import events_handlers
from app.src.events_handler import Event

class Player:

    def __init__(self, name, **kwargs):
        self.events_handler = events_handlers.main_events_handler

        self.events_infos = {
            "Dungeon.Player.LevelUp":{
                "ancient_level":None, 
                "new_level":None,
            },
            "Dungeon.Player.GetXP":{
                "xp":None,
            },
            "Dungeon.Player.StatChanged":{
                "name":None,
                "ancient_value":None,
                "new_value":None,
            },
        }

        for event_name, event_kw in self.events_infos.items():
            event = Event(event_name, **event_kw)
            self.events_handler.add_event(event)
            
        self.name = name
        self.level = kwargs.get("level", 0)
        self.xp = kwargs.get("xp", 0)
        self.total_xp = kwargs.get("total_xp", 0)
        self.xp_for_levelup = kwargs.get("xp_for_levelup", 10)
        self.xp_growth = kwargs.get("xp_growth", "+10")
        self.max_hp = kwargs.get("max_hp", 50)
        self.hp = kwargs.get("hp", self.max_hp)
        self.max_strength = kwargs.get("max_strength", 10)
        self.strength = kwargs.get("strength", self.max_strength)
        self.max_defense = kwargs.get("max_defense", 5)
        self.defense = kwargs.get("defense", self.max_defense)

    def add_xp(self, xp: int|float, add_to_total: bool=True):
        self.xp += xp

        if add_to_total:
            self.total_xp += xp

        if self.xp < 0:
            self.xp = 0

        if self.xp >= self.xp_for_levelup:
            diff = self.xp - self.xp_for_levelup
            print(diff)
            self.levelup(1)
            self.add_xp(diff, add_to_total=False)

        self.events_handler.raise_event("Dungeon.Player.GetXP", xp=xp)
    
    def levelup(self, lvl_count: int, reset_xp: bool=True):
        print("Level up")
        ancient_level = self.level
        self.level += lvl_count
        self.xp_for_levelup = int(eval(f"{self.xp_for_levelup}{self.xp_growth}"))

        if reset_xp:
            self.xp = 0
        self.events_handler.raise_event("Dungeon.Player.LevelUp", ancient_lvl=ancient_level, new_level=self.level)
