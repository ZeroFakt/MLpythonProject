from datetime import datetime

from models.enums import TransactionType
from models.ml_model import MLModel
from models.transaction import Transaction
from models.user import User, Admin
from services.prediction_service import PredictionService, execute_task
from services.validation_service import DataValidationService


def main():
    # 1. Создание пользователей
    user = User(user_id=1, username="test_user", password_hash="hashed_password", balance=100.0, role="USER")
    admin = Admin(user_id=2, username="admin", password_hash="admin_password", balance=500.0)

    print(f"Пользователь создан: {user}")
    print(f"Администратор создан: {admin}")

    # 2. Пополнение баланса пользователем
    print("\nПополнение баланса пользователем:")
    user.deposit(50.0)
    print(f"Баланс пользователя после пополнения: {user.balance}")

    # 3. Администратор изменяет баланс пользователя
    print("\nАдминистратор изменяет баланс пользователя:")
    admin.adjust_user_balance(user, 25.0)
    print(f"Баланс пользователя после изменений: {user.balance}")

    # 4. Создание транзакции
    print("\nСоздание транзакции:")
    transaction = Transaction(
        transaction_id=1,
        user_id=user.user_id,
        amount=25.0,
        transaction_type=TransactionType.DEBIT,
        timestamp=datetime.now()
    )
    print(f"Транзакция создана: {transaction}")

    # 5. Валидация данных
    print("\nВалидация данных:")
    data_list = ["123", "456.78", "abc", "0.99", "invalid"]
    validator = DataValidationService()
    valid_data, invalid_data = validator.filter_invalid_data(data_list)
    print("Валидные данные:", valid_data)
    print("Невалидные данные:", invalid_data)

    # 6. Работа с ML задачами
    print("\nСоздание и выполнение задачи предсказания:")
    ml_model = MLModel(
        model_id=1,
        name="Test ML Model",
        description="This is a test ML model.",
        cost_per_prediction=10.0,
        version="1.0"
    )
    prediction_service = PredictionService(model=ml_model)

    # Входные данные для задачи
    input_data = "Sample input data for prediction"

    try:
        prediction_task = prediction_service.create_prediction_task(user, input_data)
        # Выполняем задачу
        result = execute_task(prediction_task)
        print(f"Результат предсказания: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")

    # 7. Просмотр истории транзакций
    print("\nПросмотр всех транзакций:")
    transactions = [
        Transaction(
            transaction_id=1,
            user_id=user.user_id,
            amount=50.0,
            transaction_type=TransactionType.CREDIT,
            timestamp=datetime.now()
        ),
        Transaction(
            transaction_id=2,
            user_id=user.user_id,
            amount=25.0,
            transaction_type=TransactionType.DEBIT,
            timestamp=datetime.now()
        ),
    ]
    all_transactions = admin.view_all_transactions(transactions)
    for t in all_transactions:
        print(t)


if __name__ == "__main__":
    main()
