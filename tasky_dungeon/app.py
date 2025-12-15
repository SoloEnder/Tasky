
from app.tasky_dungeon.utils import events_handler_portal

class TaskyDungeon:

    def __init__(self, master):
        self.app = app
        self.events_handler = events_handler_portal.main_events_handler
        self.events_infos = {
            "TaskyDungeon.System.InstanceInitialised":{
                "instance":None,
                },
            }
        self.set_events(self.events_infos)

    def set_events(self, events_kw: dict):

        for event_name, event_kw in events_kw:
            event = events_handler_portal.Event(event_name, **event_kw)
            self.events_handler.add_event(event)
