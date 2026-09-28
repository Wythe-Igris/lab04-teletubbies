import pytest
from bank import BankAccount


@pytest.fixture
def account():
    return BankAccount(100)


def test_withdraw_reduces_balance(account):
    result = account.withdraw(30)
    assert result == 70
    assert account.balance == 70


def test_overdraft_raises_value_error(account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(101)
    assert account.balance == 100
