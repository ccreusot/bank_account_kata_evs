import unittest
from unittest.mock import Mock
from balance_manager import BalanceManager
from event_dispatcher import EventDispatcher
from transaction import TransactionRequested

class EventDispatcherTest(unittest.TestCase):
    
    def test_when_it_receive_a_transaction_request_event_it_should_dispatch_it_to_the_balance_manager(self):
        balance_manager = BalanceManager()
        balance_manager.compute_on_transaction = Mock()

        event = EventDispatcher(balance_manager)

        transaction = TransactionRequested(accountID="accountId", amount=10)

        event.receive(transaction)

        balance_manager.compute_on_transaction.assert_called()


if __name__ == '__main__':
    unittest.main()