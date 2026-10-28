# Lab 5: Static Code Analysis

**Student:** Atharva Anand  
**SRN:** PES1UG24CS092  
**Assigned repository:** `SETAPESU26/L5_34_online_exam`

This submission applies Pylint, Bandit, and Flake8 to the assigned online
examination program. It preserves the original reports, documents the issues,
contains the cleaned program, and includes the verified final reports.

## Contents

- `online_exam.py` - cleaned online examination program
- `issues.md` - identified issues and fixes
- `reflection.md` - answers to four reflection questions
- `reports/before/` - reports from the assigned starter code
- `reports/after/` - reports from the final cleaned code

## Run

```bash
python3 online_exam.py
```

## Reproduce the final analysis

```bash
python3 -m pylint online_exam.py
python3 -m bandit -r online_exam.py
python3 -m flake8 online_exam.py
```
