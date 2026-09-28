def test_deposit_then_withdraw(funded_account):
    funded_account.deposit(200)
    funded_account.withdraw(300)
    assert funded_account.balance == 900


def test_withdraw_entire_balance(funded_account):
    funded_account.withdraw(1000)
    assert funded_account.balance == 0
