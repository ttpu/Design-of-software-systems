# Task 6 (L): square is not a rectangle (in code)


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


# First version (wrong): Square inherits from Rectangle.
class BadSquare(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width  # a square must stay a square

    def set_height(self, height):
        self.width = height
        self.height = height


def check(r):
    r.set_width(5)
    r.set_height(4)
    assert r.area() == 20, r.area()


# Fixed version: both are just shapes, there are no setters.
class Shape:
    def area(self):
        raise NotImplementedError


class Rect(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


def demo():
    print("Task 6 (L): square is not a rectangle")
    check(Rectangle())
    print("  check(Rectangle()) passes")
    try:
        check(BadSquare())
    except AssertionError as error:
        print("  check(BadSquare()) -> AssertionError:", error)
    print("  Square(4).area():", Square(4).area())


if __name__ == "__main__":
    demo()
