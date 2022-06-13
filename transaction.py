import uuid
import datetime

class _TransactionEvent:
    def __init__(self, uuid = uuid.uuid4(), accountID = None, amount = None, date = datetime.date.today(), transactionID=None):
        self.uuid = uuid
        self.accountID = accountID
        self.date = date
        self.amount = amount
        self.transactionID = transactionID


class TransactionAccepted(_TransactionEvent):
    pass

class TransactionDeclined(_TransactionEvent):
    pass

class TransactionRequested(_TransactionEvent):
    pass

