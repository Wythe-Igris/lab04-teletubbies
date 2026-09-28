import pytest
from bank import BankAccount


@pytest.fixture
def account():
    print("[setup]")
    yield BankAccount(100)
    print("[teardown]")


def test_deposit_with_yield_fixture(account):
    account.deposit(25)
    assert account.balance == 125


def test_withdraw_with_yield_fixture(account):
    account.withdraw(40)
    assert account.balance == 60
