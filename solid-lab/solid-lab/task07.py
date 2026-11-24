# Task 7 (I): split the fat interface
#
# Before: Machine had print(), scan() and fax(), so a simple printer had to
# have empty scan() and fax(). Now there are small interfaces.
# (fax() is not used in this lab, so there is no Fax interface.)

from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self, text):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass


class SimplePrinter(Printer):
    def print(self, text):
        return f"printing: {text}"


class OfficeMachine(Printer, Scanner):
    def print(self, text):
        return f"printing: {text}"

    def scan(self):
        return "scanning a page"


def demo():
    print("Task 7 (I): split the fat interface")
    machine = OfficeMachine()
    print("  OfficeMachine print:", machine.print("hello"))
    print("  OfficeMachine scan:", machine.scan())
    try:
        SimplePrinter().scan()
    except AttributeError as error:
        print("  SimplePrinter().scan() -> AttributeError:", error)


if __name__ == "__main__":
    demo()
