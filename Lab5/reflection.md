# Lab 5 Reflection

**Student:** Atharva Anand  
**SRN:** PES1UG24CS092

The supplied handout asks for four reflection answers but does not state the
questions on its three pages. The following four questions are aligned with
the handout's objective and learning outcomes.

## 1. How do Pylint, Bandit, and Flake8 differ, and why are all three useful?

Pylint focuses on broad code quality. It detects possible bugs, maintainability
problems, naming inconsistencies, missing documentation, and refactoring
opportunities. In this program it found the shared mutable default dictionary,
camelCase names, the index-based loop, and unnecessary branches.

Bandit concentrates on security patterns. It identified the weak MD5 digest,
the shell-command injection risk, the hard-coded password, and the predictable
random choice. Flake8 checks concise style and syntax rules, such as whitespace,
blank lines, and line length. The tools complement each other because a program
can be well formatted but insecure, or secure but difficult to maintain.

## 2. How were the findings prioritized and fixed?

The high-severity Bandit findings were addressed first because weak hashing and
shell injection can create real security risks. The low-severity Bandit
findings were also removed so that the final security scan was clean. Next, the
correctness issue involving the mutable default dictionary was fixed because it
could leak penalty state between calls. Naming, documentation, loop structure,
and branching were then improved for maintainability. Finally, Flake8 spacing
and line-length violations were corrected.

This order follows a risk-based approach: security and incorrect behaviour are
more urgent than cosmetic consistency, although all findings matter in a
maintained codebase.

## 3. What did static analysis reveal, and what can it not prove?

Static analysis exposed defects without executing the file. The mutable default
argument is a good example: the program's short demonstration appears to work,
but repeated calls can share hidden state. Bandit similarly detected a command
injection path in a helper that the demonstration never calls.

The tools cannot prove that the business rules are correct. They do not know
whether the grading thresholds are fair, whether every question should have the
same weight, or whether tie-breaking for the topper matches the requirements.
They also cannot fully confirm runtime behaviour. Unit tests, boundary tests,
domain review, and code review are still required alongside static analysis.

## 4. How should static analysis be used in a development workflow?

Fast checks such as Flake8 can run before each commit, while Pylint and Bandit
can run on every pull request in continuous integration. A project can reject a
change when Flake8 reports a violation, Bandit finds an unacceptable security
issue, or Pylint falls below an agreed threshold such as 9.5.

Teams should keep the rule set practical, document justified exceptions, and
avoid disabling warnings without investigation. Saving before-and-after
reports, as in this lab, makes the improvement measurable and gives reviewers
evidence that each fix was verified.
