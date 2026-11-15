import pytest

from s01_classes_basics import BankAccount, Rectangle


# ---------- Rectangle
def test_rectangle_area_perimeter():
    r = Rectangle(3, 4)
    assert r.area() == 12
    assert r.perimeter() == 14


def test_rectangle_is_square():
    assert Rectangle(5, 5).is_square() is True
    assert Rectangle(5, 6).is_square() is False


def test_rectangle_scale_in_place():
    r = Rectangle(2, 3)
    result = r.scale(2)
    assert result is None
    assert (r.width, r.height) == (4, 6)


def test_rectangle_repr():
    assert repr(Rectangle(3, 4)) == "Rectangle(width=3, height=4)"


def test_objects_are_independent():
    a, b = Rectangle(1, 1), Rectangle(1, 1)
    a.scale(10)
    assert b.width == 1


# ---------- BankAccount
def test_account_defaults():
    acc = BankAccount("Vimal")
    assert acc.owner == "Vimal"
    assert acc.balance == 0
    assert acc.transactions == []


def test_deposit_and_withdraw():
    acc = BankAccount("Vimal", 100)
    acc.deposit(50)
    acc.withdraw(30)
    assert acc.balance == 120
    assert acc.transactions == [("deposit", 50), ("withdraw", 30)]


@pytest.mark.parametrize("bad", [0, -10])
def test_invalid_amounts_raise(bad):
    acc = BankAccount("Vimal", 100)
    with pytest.raises(ValueError):
        acc.deposit(bad)
    with pytest.raises(ValueError):
        acc.withdraw(bad)
    assert acc.balance == 100
    assert acc.transactions == []


def test_insufficient_funds():
    acc = BankAccount("Vimal", 10)
    with pytest.raises(ValueError, match="Insufficient funds"):
        acc.withdraw(11)
    assert acc.balance == 10


def test_transfer():
    a, b = BankAccount("A", 100), BankAccount("B")
    a.transfer_to(b, 40)
    assert (a.balance, b.balance) == (60, 40)
    assert a.transactions == [("withdraw", 40)]
    assert b.transactions == [("deposit", 40)]


def test_failed_transfer_changes_nothing():
    a, b = BankAccount("A", 10), BankAccount("B")
    with pytest.raises(ValueError):
        a.transfer_to(b, 50)
    assert (a.balance, b.balance) == (10, 0)
    assert b.transactions == []


def test_trap_mutable_default_not_shared():
    a, b = BankAccount("A"), BankAccount("B")
    a.deposit(5)
    assert b.transactions == [], "transactions list is shared — mutable default trap!"


def test_account_repr():
    assert repr(BankAccount("Vimal", 150)) == "BankAccount(owner='Vimal', balance=150)"
