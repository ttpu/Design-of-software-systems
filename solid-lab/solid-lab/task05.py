# Task 5 (L): penguin must not fly
#
# Before: Penguin(Bird) had fly() that raised RuntimeError, so code that
# worked with any Bird could crash. Now only birds that can fly have fly().


class Bird:
    def walk(self) -> str:
        return "walking"


class FlyingBird(Bird):
    def fly(self) -> str:
        return "flying"


class Sparrow(FlyingBird):
    pass


class Penguin(Bird):
    pass


def make_fly(b: FlyingBird) -> None:
    print(b.fly())


def demo() -> None:
    print("Task 5 (L): penguin must not fly")
    print("  sparrow:", end=" ")
    make_fly(Sparrow())
    penguin = Penguin()
    print("  penguin walk():", penguin.walk())
    print("  penguin has fly():", hasattr(penguin, "fly"))
    # mypy check (optional): uncomment the next line and run  mypy task05.py
    # make_fly(Penguin())


if __name__ == "__main__":
    demo()
