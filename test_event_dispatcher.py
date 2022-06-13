import unittest
from unittest.mock import Mock
from balance_manager import BalanceManager
from event_dispatcher import EventDispatcher
from transaction import TransactionAccepted, TransactionDeclined, TransactionRequested

class EventDispatcherTest(unittest.TestCase):
    
    def test_when_it_receive_a_transaction_request_event_it_should_dispatch_it_to_the_balance_manager(self):
        transactions = [
            TransactionRequested(uuid = "uuid1", accountID="accountId", amount=10),
            TransactionDeclined(uuid = "uuid2", transactionID="uuid1"),
            TransactionRequested(uuid = "uuid3", accountID="accountId", amount=-10),
            TransactionAccepted(uuid = "uuid4", transactionID="uuid3"),
        ]

        for transaction in transactions:
            with self.subTest(transaction = transaction):
                balance_manager = BalanceManager()
                balance_manager.compute_on_transaction = Mock()
                event_dispatcher = EventDispatcher(balance_manager)
                event_dispatcher.receive(transaction)
                balance_manager.compute_on_transaction.assert_called_once()
                

if __name__ == '__main__':
    unittest.main()