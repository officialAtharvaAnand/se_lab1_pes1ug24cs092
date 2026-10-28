# Identified Issues and Fixes

**Student:** Atharva Anand  
**SRN:** PES1UG24CS092

Line numbers refer to the assigned starter version of `online_exam.py`.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Weak MD5 digest (`B324`) | Bandit - High severity | 16 | MD5 is a weak hash and is unsuitable when answers need a collision-resistant digest. | Replaced `hashlib.md5` with `hashlib.sha256`. |
| Shell command injection (`B605`) | Bandit - High severity | 56 | Concatenating `labPc` into `os.system` lets untrusted text change the shell command. | Removed the unused remote lock helper and the `os` import, eliminating the shell execution path. |
| Hard-coded password (`B105`) | Bandit - Low severity | 11 | A plaintext proctor password was stored directly in source and was not used by the program. | Removed the unused credential constant. |
| Non-cryptographic random choice (`B311`) | Bandit - Low severity | 20 | `random.choice` is predictable and is not appropriate for an exam question selection. | Replaced it with `secrets.choice`. |
| Mutable default argument (`W0102`) | Pylint - Correctness | 23 | The default `penalties={}` dictionary is created once and shared across calls. | Changed the default to `None` and created a fresh dictionary inside the function. |
| Non-PEP 8 names (`C0103`) | Pylint - Convention | 15-54 | Functions and arguments used camelCase names, which reduced consistency and readability. | Renamed functions and arguments to descriptive `snake_case` names and updated all calls. |
| Index-based loop (`C0200`) | Pylint - Refactor | 25-30 | Iterating with `range(len(QUESTIONS))` required repeated indexing. | Used `enumerate(QUESTIONS)` to obtain each index and question directly. |
| Unnecessary `elif` and `else` (`R1705`) | Pylint - Refactor | 37-42 | Branches followed unconditional returns, adding avoidable nesting. | Used independent `if` checks followed by a final return. |
| Missing documentation (`C0114`, `C0116`) | Pylint - Convention | 1, 15-59 | The module and its functions had no docstrings. | Added a module docstring and concise function docstrings. |
| Spacing and long-line violations (`E225`, `E261`, `E501`) | Flake8 - Style | 67, 69-70 | Assignment spacing, comment spacing, and a 93-character print statement violated PEP 8. | Added the required spaces and split the long call across readable lines. |

## Verification Summary

| Tool | Before | After |
|---|---:|---:|
| Pylint | 5.65/10 | 10.00/10 |
| Bandit | 4 findings (2 high, 2 low) | 0 findings |
| Flake8 | 4 violations | 0 violations |

The final program retains the original demonstration results: Anil scores 2,
Divya scores 4, Sameer scores 0, the class average is 2.0, and Divya is the
topper. The randomly selected bonus-question text can vary between runs.
