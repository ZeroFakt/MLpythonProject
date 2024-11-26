from models.enums import TransactionType
from datetime import datetime



class Transaction:
    def __init__(self, transaction_id: int, user_id: int, amount: float, timestamp: datetime, transaction_type: TransactionType):
        self._transaction_id = transaction_id
        self._user_id = user_id
        self._amount = amount
        self._timestamp = timestamp or datetime.now()
        self._transaction_type = transaction_type

    @property
    def transaction_id(self):
        return self._transaction_id

    @property
    def user_id(self):
        return self._user_id

    @property
    def amount(self):
        return self._amount

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def transaction_type(self):
        return self._transaction_type