#!/bin/bash
pytest -k test_scripts/test_*.py -vvv --html=reports/index.html --self-contained-html
find . | grep -E "(__pycache__|\.pytest|\.pyc|\.pyo$)" | xargs rm -rf