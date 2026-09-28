import pytest
from bank import BankAccount


@pytest.fixture
def account():
    return BankAccount(100)


def test_deposit_increases_balance(account):
    result = account.deposit(50)
    assert result == 150
    assert account.balance == 150


def test_multiple_deposits_accumulate(account):
    account.deposit(20)
    account.deposit(30)
    assert account.balance == 150
