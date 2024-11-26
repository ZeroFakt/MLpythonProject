from enum import Enum



class Role(Enum):
    USER = "user"
    ADMIN = "admin"


class TransactionType(Enum):
    CREDIT = "credit"
    DEPOSIT = "deposit"
    PREDICTION = "prediction"
    DEBIT = "debit"


class PredictionStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"