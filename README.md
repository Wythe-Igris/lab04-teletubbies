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

## Our Merge Conflict

Group members committed their contribution rows to the same README table from different local histories. When we pulled teammates' changes, Git reported a content conflict because it could not automatically combine the overlapping edits.

The following historical excerpt records the Igris/VII conflict shown in our saved screenshot. It is quoted evidence, not an unresolved conflict in this README:

```text
<<<<<<< HEAD
|Theikdi Nyan|Wythe-Igris|test_deposit.py|
=======
|---|---|---|
| Lin Khant Pyae (VII) | Vii1nonly | conftest.py — added reusable funded account fixture |
>>>>>>> 4a60421908175a936d85300ceaeb1bcd7a0d778d
```

We kept both members' rows, placed the table separator directly below the header, and removed the active conflict markers. We then staged README.md, committed the resolution, and pushed it. Further conflicts involved Erik/Karlos and Nick/William; their resolutions preserved the existing rows and added the remaining members' rows. The completed table contains all six members.

The resolutions are recorded in merge commits `ef87a32` (Igris/VII), `97ed0a6` (Erik/Karlos), and `8136c20` (Nick/William).