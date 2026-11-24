# Task 2 (S): find the actors
#
# Before: one class with three actors.
#
# class UserManager:
#     # actor: the user (or the security team that decides the login rules)
#     def login(self, name, password): ...
#     # actor: the support team (they decide what the reset email says)
#     def send_reset_email(self, email): ...
#     # actor: the finance department (they decide how the bill is counted)
#     def bill_monthly(self, name, amount): ...
#
# Now: one class for each actor.


class Auth:
    # actor: the user / the security team
    def __init__(self, users):
        self.users = users  # {name: password}, plain text only because it is a lab

    def login(self, name, password):
        return self.users.get(name) == password


class Mailer:
    # actor: the support team
    def send_reset_email(self, email):
        print(f"  reset email sent to {email}")


class Billing:
    # actor: the finance department
    def bill_monthly(self, name, amount):
        print(f"  {name} must pay {amount} sum this month")


def demo():
    print("Task 2 (S): find the actors")
    auth = Auth({"ali": "1234"})
    print("  right password:", auth.login("ali", "1234"))
    print("  wrong password:", auth.login("ali", "0000"))
    Mailer().send_reset_email("ali@mail.uz")
    Billing().bill_monthly("ali", 49_000)


if __name__ == "__main__":
    demo()
