
class Event:

    def __init__(self, name: str, **kwargs):
        self.name = name
        self.listeners = []
        self.kwargs = kwargs

class EventImitation:

    def __init__(self, event, **kwargs):
        self.name = event
        self.kwargs = kwargs

class EventsHandler:

    def __init__(self):
        self.current_event = ""
        self.events = {}

    def add_event(self, event):

        if not event.name in self.events.keys():
            self.events[event.name] = event
        
    def add_listener(self, event_name: str, func):

        if event_name in self.events.keys():
            event = self.events[event_name]
            event.listeners.append(func)

            return f"{event_name}:{len(event.listeners)}"

        else:
            raise ValueError(f"Event {event_name} not found !")
    
    def raise_event(self, event_name: str, **kwargs):

        if event_name in self.events.keys():
            event = self.events[event_name]

            for arg in kwargs:

                if not arg in event.kwargs.keys():
                    raise ValueError(f"Event '{event.name}' got an unexpected argument '{arg}'")
                
            else:

                for listener in event.listeners:
                    event_mimic = EventImitation(event.name, **kwargs)
                    listener(event_mimic)

        else:
            raise ValueError(f"Unknown event '{event_name}'")

    def remove_listener(self, id: str):
        event_name, index = id.split(":")
        index = int(index) - 1

        try:
            del self.events[event_name].listeners[index]

        except IndexError:
            raise ValueError(f"Unknwon event listener id '{id}'")


base_event = Event("PermissionDenied", permission=None)
eh = EventsHandler()
event = eh.add_event(base_event)
id = eh.add_listener("PermissionDenied", lambda event: print(event.name, event.kwargs["permission"]))
eh.raise_event("PermissionDenied", permission="WriteFile")
eh.remove_listener(id)
eh.raise_event("PermissionDenied")