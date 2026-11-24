# Task 9 (D): invert OrderService
#
# Before: OrderService did  self.db = MySQLDatabase()  in __init__.
# Now OrderService gets the repository from outside, and it only knows the
# OrderRepository interface. main.py chooses the real one.

from abc import ABC, abstractmethod


class OrderRepository(ABC):
    @abstractmethod
    def add(self, order):
        pass


class OrderService:
    def __init__(self, repo):
        self.repo = repo

    def place(self, order):
        if not order:
            raise ValueError("order is empty")
        self.repo.add(order)


class FileOrders(OrderRepository):
    def __init__(self, filename="orders.txt"):
        self.filename = filename

    def add(self, order):
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(f"{order}\n")


class ConsoleOrders(OrderRepository):
    def add(self, order):
        print(f"  order: {order}")


def demo(repo):
    print("Task 9 (D): invert OrderService")
    service = OrderService(repo)
    service.place("order-17")
    print(f"  order-17 placed with {type(repo).__name__}")
    try:
        service.place("")
    except ValueError as error:
        print("  empty order ->", error)


if __name__ == "__main__":
    demo(ConsoleOrders())
