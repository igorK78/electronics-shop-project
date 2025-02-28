import csv
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name if len(name) <= 10 else 'Exception: Длина наименования товара превышает 10 символов.'

    @classmethod
    def instantiate_from_csv(cls):
        Item.all.clear()
        with open('../src/items.csv', 'r') as file:
            items = csv.DictReader(file)
            for row in items:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(number: str) -> int:
        return int(float(number))
