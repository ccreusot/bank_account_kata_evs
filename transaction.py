import uuid
import datetime

class _TransactionEvent:
    def __init__(self, accountID, amount, date = datetime.date.today(), transactionID=None):
        self.uuid = uuid.uuid4()
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

