def test_shared_account_deposit(funded_account):
    funded_account.deposit(100)
    assert funded_account.balance == 1100


def test_shared_account_withdraw(funded_account):
    funded_account.withdraw(250)
    assert funded_account.balance == 750
