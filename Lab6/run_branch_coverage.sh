#!/bin/sh
set -eu
cd "$(dirname "$0")"
printf '\033[2J\033[H\033[3J'
printf 'Lab 6 - branch coverage\n\n'
python -m coverage run --branch --source=tennis_scoring -m pytest -q BranchCoverageTest_tennis_scoring_application.py
python -m coverage report -m
