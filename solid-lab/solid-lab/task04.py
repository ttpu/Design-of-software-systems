# Task 4 (O): add a new discount
#
# Nothing in task03.py is changed. The new discount is only added here.

from task03 import Bogo, Percent, final_price


class StudentDiscount(Percent):
    def __init__(self):
        super().__init__(15)


# the only place that decides which kind gives which class
DISCOUNTS = {
    "bogo": Bogo,
    "student": StudentDiscount,
}


def make_discount(kind):
    if kind not in DISCOUNTS:
        raise ValueError("unknown discount")
    return DISCOUNTS[kind]()


def demo():
    print("Task 4 (O): add a new discount")
    discount = make_discount("student")
    print("  student on 200_000:", f"{final_price(200_000, discount):,.0f}")
    try:
        make_discount("vip")
    except ValueError as error:
        print("  kind 'vip' ->", error)


if __name__ == "__main__":
    demo()
