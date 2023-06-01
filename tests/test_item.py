"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item3 = Item('Кабель', 10, 5)


def test_item_init():
    assert item3.name == "Кабель"
    assert item3.price == 10
    assert item3.quantity == 5


def test_calculate_total_price():
    assert item3.calculate_total_price() == 50


def test_apply_discount():
    Item.pay_rate = 0.8
    item3.apply_discount()
    assert item3.price == 8