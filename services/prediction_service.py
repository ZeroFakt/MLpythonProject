import random
from datetime import datetime

from models.ml_model import MLModel
from models.prediction_task import PredictionTask
from models.user import User
from utils.exceptions import InsufficientBalanceException


def execute_task(task: PredictionTask) -> str:
    """Выполняет задачу предсказания и возвращает результат."""
    # Симуляция выполнения предсказания
    result = f"Предсказание для задачи {task.task_id} выполнено успешно. Входные данные: {task.input_data}"
    return result


class PredictionService:
    def __init__(self, model: MLModel):
        self.model = model

    def create_prediction_task(self, user: User, input_data: str) -> PredictionTask:
        """Создает задачу предсказания, списывая средства с баланса."""
        if user.deduct_credits(self.model.cost_per_prediction):
            task = PredictionTask(
                task_id=self._generate_task_id(),
                user_id=user.user_id,
                model_id=self.model.model_id,
                input_data=input_data,
                created_date=datetime.now()
            )
            return task
        else:
            raise InsufficientBalanceException("Недостаточно кредитов для выполнения запроса.")

    @staticmethod
    def _generate_task_id():
        """Генерация уникального ID задачи."""
        return random.randint(100000, 999999)
