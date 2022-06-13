import unittest
from unittest.mock import Mock
from balance_manager import BalanceManager
from event_dispatcher import EventDispatcher
from transaction import TransactionAccepted, TransactionDeclined, TransactionRequested

class EventDispatcherTest(unittest.TestCase):

    def test_when_emit_event_that_dispatcher_saves_it(self):
        event_dispatcher = EventDispatcher()
        transaction = TransactionRequested()
        event_dispatcher.emit(transaction)
        self.assertEqual(event_dispatcher._events_list, [transaction])

    def test_when_subscribed_for_event_hasndler_should_be_called_once(self):
        event_dispatcher = EventDispatcher()
        transaction = TransactionRequested()
        handler = Mock()
        event_dispatcher.subscribe(TransactionRequested, handler)
        event_dispatcher.emit(transaction)

        handler.assert_called_once()

    def test_when_multiple_subscriber_for_event_type_all_should_be_called_once(self):
        event_dispatcher = EventDispatcher()
        transaction = TransactionRequested()
        handler1 = Mock()
        handler2 = Mock()
        handler3 = Mock()
        event_dispatcher.subscribe(TransactionRequested, handler1)
        event_dispatcher.subscribe(TransactionRequested, handler2)
        event_dispatcher.subscribe(TransactionRequested, handler3)

        event_dispatcher.emit(transaction)

        handler1.assert_called_once()
        handler2.assert_called_once()
        handler3.assert_called_once()

if __name__ == '__main__':
    unittest.main()