# Task 1 (S): split the class
#
# Before: class Invoice had total(), save() and to_html() together.
# Now every class has one job.


class Invoice:
    """Only calculates the total."""

    def __init__(self, items):
        if not items:
            raise ValueError("items are empty")
        self.items = items  # list of (price, qty)

    def total(self):
        return sum(price * qty for price, qty in self.items)


class InvoiceFile:
    """Only saves the total to a file."""

    def __init__(self, filename="invoices.csv"):
        self.filename = filename

    def save(self, invoice):
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(f"{invoice.total()}\n")


class InvoiceHtml:
    """Only makes the html."""

    def to_html(self, invoice):
        return f"<h1>Total: {invoice.total()}</h1>"


def demo():
    print("Task 1 (S): split the class")
    invoice = Invoice([(10_000, 2), (5_000, 1)])
    print("  total:", invoice.total())
    print("  html:", InvoiceHtml().to_html(invoice))
    InvoiceFile().save(invoice)
    print("  saved to invoices.csv")
    try:
        Invoice([])
    except ValueError as error:
        print("  empty items ->", error)


if __name__ == "__main__":
    demo()
