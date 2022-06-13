class EventDispatcher:

    def __init__(self, balance_manager):
        self._balance_manager = balance_manager

    def receive(self, event):
        self._balance_manager.compute_on_transaction(event)