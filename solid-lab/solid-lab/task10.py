# Task 10 (D): test with a fake
#
# Run:  pytest task10.py

import pytest

from task09 import OrderRepository, OrderService


class FakeOrders(OrderRepository):
    """Keeps orders in a list, so the test needs no file."""

    def __init__(self):
        self.saved = []

    def add(self, order):
        self.saved.append(order)


def test_place_saves_the_order_in_the_repo():
    repo = FakeOrders()
    service = OrderService(repo)
    service.place("order-17")
    assert repo.saved == ["order-17"]


def test_empty_order_raises_value_error():
    service = OrderService(FakeOrders())
    with pytest.raises(ValueError):
        service.place("")


def demo():
    print("Task 10 (D): test with a fake")
    repo = FakeOrders()
    OrderService(repo).place("order-17")
    print("  FakeOrders.saved:", repo.saved)
    print("  (run  pytest  to see the tests)")


if __name__ == "__main__":
    demo()
