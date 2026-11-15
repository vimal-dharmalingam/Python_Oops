"""
SESSION 1 — Classes, __init__, self, instance methods, __repr__
================================================================

10-MIN LESSON (read first)
--------------------------
You already write functions that pass data around:
    def deposit(account_dict, amount): account_dict["balance"] += amount

A class bundles the DATA and the FUNCTIONS that work on it into one thing:

    class Account:
        def __init__(self, owner, balance=0):   # runs when you create an object
            self.owner = owner                   # instance attribute (per object)
            self.balance = balance

        def deposit(self, amount):               # instance method
            self.balance += amount

        def __repr__(self):                      # what you see when you print / debug
            return f"Account(owner={self.owner!r}, balance={self.balance})"

    a = Account("Vimal", 100)    # Python calls Account.__init__(a, "Vimal", 100)
    a.deposit(50)                # Python calls Account.deposit(a, 50)

Key ideas:
  * `self` is just "this particular object". Python passes it automatically.
  * Every object has its OWN copy of attributes set on `self`.
  * __init__ initialises; it does not return anything.
  * __repr__ should look like the code that would recreate the object.

INTERVIEW TRAP #1: mutable default arguments.
    def __init__(self, items=[]):   # WRONG — the same list is shared by ALL objects
    def __init__(self, items=None): # RIGHT
        self.items = items if items is not None else []

RULES
-----
Write the classes below, then from the Python_Oops folder run:
    pip install -r requirements.txt     (first time only)
    pytest 01_classes_objects -v
All tests must be green.
"""


# EXERCISE 1 — warm-up
# Rectangle(width, height)
#   .area()       -> width * height
#   .perimeter()  -> 2 * (width + height)
#   .is_square()  -> True if width == height
#   .scale(factor) -> multiplies width and height IN PLACE, returns nothing
#   repr -> "Rectangle(width=3, height=4)"
class Rectangle:
    pass


# EXERCISE 2 — the real one
# BankAccount(owner, balance=0, transactions=None)
#   .owner, .balance, .transactions (a list of tuples like ("deposit", 50))
#
#   .deposit(amount)
#       amount must be > 0, otherwise raise ValueError
#       adds to balance, records ("deposit", amount)
#   .withdraw(amount)
#       amount must be > 0, otherwise raise ValueError
#       if amount > balance raise ValueError("Insufficient funds")
#       subtracts, records ("withdraw", amount)
#   .transfer_to(other_account, amount)
#       withdraw from self, deposit into other  (reuse your own methods!)
#       records nothing extra — the withdraw/deposit records are enough
#   repr -> "BankAccount(owner='Vimal', balance=150)"
#
#   Watch out for TRAP #1 with `transactions`.
class BankAccount:
    pass


# EXERCISE 3 — explain in your own words (write as comments, Claude will review)
# Q1. What is `self`, and why must every instance method take it?
#     A:
# Q2. Difference between a class and an object?
#     A:
# Q3. Why did transfer_to reuse withdraw/deposit instead of changing balances directly?
#     A:
