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
| Lin Khant Pyae (VII) | Vii1nonly | conftest.py — integrated the reusable funded account fixture; added own README row and conflict documentation |
| Theikdi Nyan | Wythe-Igris | test_deposit.py — integrated deposit tests; set up the repository and starter README; added own row and resolved the Igris/VII conflict |
| Aung Myat Phone | therealfakeCowboy | test_withdraw.py — integrated withdrawal and overdraft tests; added own README row and reflection answers |
| Kaung Htet Hein (Erik) | erikchennnn | test_teardown.py — integrated yield-fixture tests; added own README row, resolved the Erik/Karlos conflict, and added the contribution summary |
| Min Htet Aung (Nick) | ARandomGuy9786 | test_shared.py — integrated shared-fixture tests; added own README row and resolved the Nick/William conflict |
| William | WillieNay | test_account_operations.py — integrated combined-operation and full-withdrawal tests; added own README row and merged teammates' updates |

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

## Reflection Questions

### 1. Why was your push rejected, and how did you fix it?

Our group experienced rejected pushes when teammates had already pushed commits that were missing from our local branches. We pulled the remote changes, resolved the README conflicts, committed the merges, and pushed again.

### 2. Why could Git not resolve the README conflict automatically?

Members inserted different contribution rows at the same location in the README table from a shared starting version. Git could not determine how to combine those overlapping edits, so we manually retained everyone's rows and corrected the table layout.

### 3. What is the difference between committing and pushing?

Committing records a snapshot of staged changes in your local Git repository. Pushing uploads local commits to the shared GitHub repository so teammates can access them.

### 4. How do fixtures reduce duplicated setup code in tests?

Fixtures define reusable setup that pytest supplies to tests requesting it, so each test does not need to repeat the account creation code. Our function-scoped fixtures provide a fresh account for each test, and conftest.py makes funded_account available across test files.

## Git Contribution Summary

Contribution counts at commit `a128ce3`:

```text
7  Wythe-Igris
4  Vii1nonly
4  erikchennnn
3  ARandomGuy9786
3  William Nay
3  therealfakeCowboy
```
