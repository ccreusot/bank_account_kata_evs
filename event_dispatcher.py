class EventDispatcher:
    
    def __init__(self):
        self._events_list = []
        self._handlers = []

    def emit(self, event):
        self._events_list.append(event)
        handlers = [handler for (event_type, handler) in self._handlers if event_type is type(event)]
        for handler in handlers:
            handler(event)
        
    def subscribe(self, event_type, handler):
        self._handlers.append((event_type, handler))