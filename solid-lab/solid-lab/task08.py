# Task 8 (I): Protocol
#
# Run:  mypy task08.py

from typing import Protocol


class Printer(Protocol):
    def print(self, text: str) -> None: ...


class LabelPrinter:  # no base class, it only has the right method
    def print(self, text: str) -> None:
        print(f"label: {text}")


def print_receipt(p: Printer, text: str) -> None:
    p.print(text)


def demo() -> None:
    print("Task 8 (I): Protocol")
    print("  ", end="")
    print_receipt(LabelPrinter(), "Order #17")

    # Failure path: uncomment the next 3 lines and run  mypy task08.py
    # mypy shows an error before the program runs.
    # Recovery: comment them again (or add a print() method), mypy passes.
    # class NoPrint:
    #     pass
    # print_receipt(NoPrint(), "Order #17")


if __name__ == "__main__":
    demo()
