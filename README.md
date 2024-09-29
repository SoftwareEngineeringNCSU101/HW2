# SE-hw2
Repository for SE homework 2

[![Language-Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Platform-Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://www.linux.org/)
[![GitHub license](https://img.shields.io/github/license/SoftwareEngineeringNCSU101/HW2)](https://github.com/SoftwareEngineeringNCSU101/HW2/LICENSE.md)
[![Python application](https://github.com/SoftwareEngineeringNCSU101/HW2/actions/workflows/python-test.yml/badge.svg)](https://github.com/SoftwareEngineeringNCSU101/HW2/actions/workflows/python-test.yml)

![CI](https://img.shields.io/github/actions/workflow/status/SoftwareEngineeringNCSU101/HW2/python-test.yml?branch=main)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen)](https://pre-commit.com)
[![flake8](https://img.shields.io/badge/flake8-passing-brightgreen)](https://flake8.pycqa.org)
[![pylint](https://img.shields.io/badge/pylint-passing-green)](https://github.com/SoftwareEngineeringNCSU101/HW2/actions/workflows/python-lint.yml)
[![bandit](https://img.shields.io/badge/bandit-passing-green)](https://github.com/SoftwareEngineeringNCSU101/HW2/actions/workflows/python-security.yml)

## Pre-commit hooks
This project uses [pre-commit](https://pre-commit.com) for automated code quality checks. The following hooks are configured:

- **Trailing Whitespace Removal**: Ensures no trailing whitespace.
- **End of File Fixer**: Ensures that files end with a newline.
- **Check YAML**: Verifies the syntax of YAML files.
- **AutoPEP8**: Automatically formats Python code to conform to PEP8 style guide.
- **Pylint**: Runs pylint for linting Python code.
- **Pyflakes**: Runs Pyflakes for Python syntax checks.

## CI Pipeline
This project uses GitHub Actions for Continuous Integration (CI), which includes:

- **Flake8**: Python linting for syntax errors and style violations.
- **Pytest**: Running the test suite defined in `hw2/test_cases.py`.

## How to Run
To run the pre-commit hooks locally, use:

```bash
pre-commit run --all-files
