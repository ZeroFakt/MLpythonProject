class DataValidationService:
    def __init__(self):
        pass

    @staticmethod
    def validate_data_item(data_item) -> bool:
        """
        Проверка отдельного элемента данных. Возвращает True, если данные валидны, иначе False.
        Здесь можно определить набор правил для проверки каждого элемента.
        """
        if not data_item:  # Проверка на пустоту
            return False

        if not isinstance(data_item, (int, float, str)):  # Проверка типа данных
            return False

        if isinstance(data_item, (int, float)) and (data_item < 0 or data_item > 1000):
            # Допустим, числовое значение должно быть в диапазоне от 0 до 1000
            return False

        if isinstance(data_item, str) and len(data_item) > 255:
            # Допустим, строковое значение не должно превышать 255 символов
            return False

        return True

    def validate_data(self, data: list) -> bool:
        """
        Проверка всей выборки данных. Возвращает True, если все данные валидны, иначе False.
        """
        return all(self.validate_data_item(item) for item in data)

    def filter_invalid_data(self, data: list[str]) -> tuple[list[str], list[str]]:
        """ Отделяет валидные и невалидные данные """
        valid_data, invalid_data = [], []
        for item in data:
            if self.validate_data_item(item):
                valid_data.append(item)
            else:
                invalid_data.append(item)
        return valid_data, invalid_data