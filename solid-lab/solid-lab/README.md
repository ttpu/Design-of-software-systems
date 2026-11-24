# SOLID principles: theory and practice (Laboratory work 6)

Python 3.10+. Only `pytest` and `mypy` are used. One file per task: `task01.py` ... `task10.py`.

## How to run

```
python -m venv .venv
.venv\Scripts\activate        (Windows)   or   source .venv/bin/activate   (Linux / Mac)
pip install -r requirements.txt

python main.py         # happy path: results of all 10 tasks are printed
mypy task08.py         # type check of the Protocol task
pytest                 # tests of all tasks (task10.py has the tests of Task 10)
```

`main.py` also creates `invoices.csv` (Task 1) and `orders.txt` (Task 9). They are in `.gitignore`.

## Demo video

<details>
<summary>Show / hide demo video (max 40 seconds)</summary>

<!-- Upload the .mp4 here (drag and drop it into the GitHub editor) and put the link on the next line -->

VIDEO_LINK_HERE

Scenario shown in the video, step by step:

1. **Happy path:** run `python main.py`. The results of all 10 tasks are printed.
2. **Failure path:** in `task08.py` uncomment the class `NoPrint` (3 lines in `demo()`) and run `mypy task08.py`. mypy shows an error because `NoPrint` has no `print()`.
3. **Recovery path:** comment those lines again and run `mypy task08.py`. mypy passes.
4. **Optional part:** run `pytest`, all tests pass. Then remove the line `self.repo.add(order)` from `place()` in `task09.py` and run `pytest` again. The test `test_place_saves_the_order_in_the_repo` fails. Put the line back.

</details>

### Happy / failure / recovery for every task

| Task | Happy path | Failure path | Recovery |
|---|---|---|---|
| 1 `task01.py` | total 25000, html `<h1>Total: 25000</h1>`, total saved to `invoices.csv` | `Invoice([])` raises `ValueError` | give a list with items |
| 2 `task02.py` | right password gives `True`, reset mail and monthly bill are printed | wrong password gives `False` | use the right password |
| 3 `task03.py` | on 200 000: `Percent(10)` 180 000, `Fixed(50_000)` 150 000, `Bogo()` 100 000 | `Fixed(50_000)` on 30 000 would be negative | result is 0, nothing to fix |
| 4 `task04.py` | `"student"` gives 170 000 (15% off) | `make_discount("vip")` raises `ValueError('unknown discount')` | use `"student"` or `"bogo"` |
| 5 `task05.py` | `Sparrow` prints `flying`, `Penguin` walks | `make_fly(Penguin())` (optional) gives a mypy error | comment the line, mypy passes |
| 6 `task06.py` | `check(Rectangle())` passes, `Square(4).area()` is 16 | `check(BadSquare())` gives `AssertionError: 16` | use `Square` as a sibling of `Rect` under `Shape` |
| 7 `task07.py` | `OfficeMachine` prints and scans | `SimplePrinter().scan()` gives `AttributeError` | use `OfficeMachine` when scanning is needed |
| 8 `task08.py` | `LabelPrinter` prints `label: Order #17`, mypy passes | class `NoPrint` gives a mypy error | comment it, mypy passes |
| 9 `task09.py` | `FileOrders()` writes the order to `orders.txt` | `place("")` raises `ValueError` | pass a real order |
| 10 `task10.py` | `pytest task10.py`: 2 tests pass | remove `repo.add` from `place()`, the test fails | put the line back, tests pass |

## Dependency Inversion in this repo

```
Who owns the interface:
    task09.py  ->  OrderRepository (ABC with add(order)), line 10
    It lives next to OrderService (line 16), the high-level code that needs it.
    OrderService only calls self.repo.add(order) (line 18). It never says
    FileOrders, ConsoleOrders or any database. A test checks this.

Who names the details:
    FileOrders (task09.py line 26) and ConsoleOrders (task09.py line 35)
    inherit OrderRepository. They are details, they depend on the interface.
    They are in the same file only because the lab wants one file per task.
    The only place that writes a detail name in the working code is
    main.py line 22:   orders_repo = FileOrders()
    To change the storage I change only this one line, OrderService stays the same.

Tests (task10.py):
    FakeOrders (line 10) is one more detail of the same interface.
    The test creates it and gives it to OrderService, so no file is needed.

Direction of the arrows:
    OrderService --> OrderRepository <-- FileOrders / ConsoleOrders / FakeOrders
    The high-level class does not depend on the details, the details depend on the interface.
```

## Part A. Theory

**1. (S) What is a reason to change? State Single Responsibility in one sentence.**
A reason to change is a person or a group (an actor) who can ask me to change the code, for example the finance department. Single Responsibility: a class should have only one reason to change, so it should serve only one actor.

**2. (S) Class `Report` has `calculate_totals()`, `to_pdf()` and `send_email()`. Which principle is broken? Name the actors.**
Single Responsibility is broken. The actors are the finance department (rules for the totals), the people who decide how the PDF looks (`to_pdf`) and the IT / support team that runs the mail sending (`send_email`). Each of them can ask for a change, so the class should be split into three.

**3. (O) State Open/Closed. How does a growing `if/elif` chain on a type show that it is broken?**
Open/Closed: code should be open for extension but closed for modification, so new behavior is added by writing new code and not by editing old code. If every new type adds one more `elif` to the same function, then I must edit that function again and again, so it is not closed and I can break the old branches.

**4. (O) Which tool from Lecture 4 makes Open/Closed possible? Why does "closed" not mean "never touch"?**
Abstraction with polymorphism makes it possible: an abstract class (or interface) and a new child class for every new behavior. "Closed" means I do not edit the working code to add a feature, but I can still fix bugs, and I must edit once to introduce the abstraction and the place that chooses the class (like the `DISCOUNTS` dict).

**5. (L) State Liskov Substitution in your own words. Name two of the four rules a child must keep.**
If code works with a parent class, it must work the same way when I give it any child, with no surprises. Two rules: the child must not make the preconditions stronger (it must not ask for more than the parent), and it must not make the postconditions weaker (it must promise at least what the parent promises).

**6. (L) Why is `Square(Rectangle)` a violation in code, even though it is true in geometry?**
In geometry "is a" is only about the shape, but in code `Rectangle` promises that width and height can be changed separately. `Square` has to change both together, so `set_width(5)` and `set_height(4)` give area 16 and not 20. The code that works with `Rectangle` breaks when it gets a `Square`.

**7. (I) What is a fat interface? Name two symptoms of it.**
A fat interface is a big interface with many methods, where each client needs only a part of them. Symptoms: classes have empty methods or methods that raise `NotImplementedError` because they cannot do that job, and a change in a method that a client never uses still touches that client.

**8. (I) What is the difference between ABC and Protocol?**
With ABC the class must inherit from it by name, and Python checks it when the program runs (an abstract class cannot be created if methods are missing). With Protocol a class fits if it has the right methods, no inheritance is needed, and mypy checks it before the program runs.

**9. (D) Explain DIP, DI and IoC container. How are they different?**
DIP is a principle: high-level code and low-level code should both depend on abstractions, not on concrete classes. DI is a technique: an object gets its dependencies from outside (for example in the constructor) and does not create them. An IoC container is a tool that creates the objects and gives them their dependencies automatically. So it is a principle, a technique and a tool.

**10. (D) Why is a class with `self.db = MySQLDatabase()` hard to test? How do you fix it?**
The class creates the real database by itself, so every test needs a real MySQL, it is slow, and I cannot replace it. The fix is to pass the database (as an abstraction, for example `OrderRepository`) into the constructor, and in tests I pass a fake one.

## Files

```
main.py            runs all 10 demos (happy path)
task01.py ... task10.py
tests/test_tasks.py   tests of tasks 1-9 (every "If" line of the lab)
pytest.ini         pytest settings (collects task10.py and tests/)
requirements.txt   pytest, mypy
```
