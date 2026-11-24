"""Runs the demo of all 10 tasks (happy path)."""
import sys

import task01
import task02
import task03
import task04
import task05
import task06
import task07
import task08
import task09
import task10
from task09 import ConsoleOrders, FileOrders


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    # the only place that chooses the real repository (Task 9)
    orders_repo = FileOrders()  # switch to ConsoleOrders() to print instead

    task01.demo()
    task02.demo()
    task03.demo()
    task04.demo()
    task05.demo()
    task06.demo()
    task07.demo()
    task08.demo()
    task09.demo(orders_repo)
    task10.demo()


if __name__ == "__main__":
    main()
