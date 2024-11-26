from models.enums import PredictionStatus
from datetime import datetime


class PredictionTask:
    def __init__(self, task_id: int, user_id: int, model_id: int, input_data: str, created_date: datetime):
        self._task_id = task_id
        self._user_id = user_id
        self._model_id = model_id
        self._input_data = input_data
        self._result_data = None
        self._status = PredictionStatus.PENDING
        self._created_date = created_date

    @property
    def task_id(self):
        return self._task_id

    @property
    def user_id(self):
        return self._user_id

    @property
    def model_id(self):
        return self._model_id

    @property
    def input_data(self):
        return self._input_data

    @property
    def result_data(self):
        return self._result_data

    @property
    def status(self):
        return self._status

    @property
    def created_date(self):
        return self._created_date

    def start_processing(self):
        """ Изменить статус задачи на 'В процессе' """
        self._status = PredictionStatus.IN_PROGRESS

    def complete(self, result_data: str):
        """ Завершить задачу и сохранить результат """
        self._status = PredictionStatus.COMPLETED
        self._result_data = result_data

    def fail(self):
        """ Изменить статус задачи на 'Ошибка' """
        self._status = PredictionStatus.FAILED

    def __str__(self):
        return (f"PredictionTask(task_id={self._task_id}, user_id={self._user_id}, model_id={self._model_id}, "
                f"input_data='{self._input_data}', result_data='{self._result_data}', "
                f"status={self._status}, created_date={self._created_date})")
