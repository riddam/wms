#!/bin/sh

runtest=${RUNTEST:-"no"}
PYTHONPATH="/app"

if [ "$runtest" = "yes" ]; then
  flake8 && pytest core/tests.py
else
  python main.py
fi
