# TELETUBBIES — Lab 4

192-211 Automated Software Testing.

## Setup and run

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install pytest
python -m pytest -v
python -m pytest -v -s
```

On Windows PowerShell, activate with `venv\Scripts\Activate.ps1` instead. The completed test suite contains 10 tests.

## Preparation and contributions

The initial code pack and workflow were prepared by Igris using prior class patterns and the lab's BankAccount example. Each member will integrate and test their assigned file and participate in the shared Git workflow.

## Who Did What

| Member | GitHub Username | File / Actual Contribution |
|---|---|---|
| Lin Khant Pyae (VII) | Vii1nonly | conftest.py — added reusable funded account fixture |
| Theikdi Nyan | Wythe-Igris | test_deposit.py |
| Aung Myat Phone | therealfakeCowboy | test_withdraw.py |
| Kaung Htet Hein (Erik) | erikchennnn | test_teardown.py |
| Min Htet Aung (Nick) | ARandomGuy9786 | test_shared.py |
| William | WillieNay | test_account_operations.py added |
