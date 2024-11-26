from models.enums import Role



class User:
    def __init__(self, user_id: int, username: str, password_hash: str, balance: float, role: str = "USER"):
        self._user_id = user_id
        self._username = username
        self._password_hash = password_hash
        self._balance = balance
        self._role = role


    @property
    def user_id(self):
        return self._user_id

    @property
    def username(self):
        return self._username

    @property
    def balance(self):
        return self._balance

    @property
    def role(self):
        return self._role

    def deposit(self, amount: float):
        """ Пополнение счета """
        if amount > 0:
            self._balance += amount

    def deduct_credits(self, amount: float) -> bool:
        """ Списание кредитов со счета """
        if self._balance >= amount:
            self._balance -= amount
            return True
        return False

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @username.setter
    def username(self, value):
        self._username = value

    @balance.setter
    def balance(self, value):
        self._balance = value

    @role.setter
    def role(self, value):
        self._role = value


class Admin(User):
    def __init__(self, user_id: int, username: str, password_hash: str, balance: float):
        super().__init__(user_id, username, password_hash, balance, Role.ADMIN)

    @staticmethod
    def adjust_user_balance(user: User, amount: float):
        """ Изменение баланса другого пользователя """
        user.deposit(amount)

    @staticmethod
    def view_all_transactions(transactions: list):
        """ Просмотр всех транзакций """
        return transactions