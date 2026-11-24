# Task 3 (O): open the discount system
#
# Before:
#
# def final_price(price, kind):
#     if kind == "percent": ...
#     elif kind == "fixed": ...
#     elif kind == "bogo": ...
#
# Every new discount meant editing this function. Now one class per discount.

from abc import ABC, abstractmethod


class Discount(ABC):
    @abstractmethod
    def apply(self, price):
        """Return the price after the discount."""


class Percent(Discount):
    def __init__(self, percent):
        self.percent = percent

    def apply(self, price):
        return price * (100 - self.percent) / 100


class Fixed(Discount):
    def __init__(self, amount):
        self.amount = amount

    def apply(self, price):
        return max(0, price - self.amount)  # never below zero


class Bogo(Discount):
    """Buy one get one: the price per item is half."""

    def apply(self, price):
        return price / 2


def final_price(price, discount):
    return discount.apply(price)


def demo():
    print("Task 3 (O): open the discount system")
    price = 200_000
    print("  Percent(10):", f"{final_price(price, Percent(10)):,.0f}")
    print("  Fixed(50_000):", f"{final_price(price, Fixed(50_000)):,.0f}")
    print("  Bogo():", f"{final_price(price, Bogo()):,.0f}")
    print("  Fixed(50_000) on 30_000:", f"{final_price(30_000, Fixed(50_000)):,.0f}")


if __name__ == "__main__":
    demo()
