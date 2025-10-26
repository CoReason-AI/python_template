# {{cookiecutter.project_name}}

[![PyPI Version](https://img.shields.io/pypi/v/{{cookiecutter.project_slug}})](https://pypi.org/project/{{cookiecutter.project_slug}}/)
[![Build Status](https://img.shields.io/github/actions/workflow/status/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/ci-cd.yml?branch=main)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions/workflows/ci-cd.yml)
[![codecov](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}})
[![License](https://img.shields.io/badge/License-Prosperity%203.0.0-blue.svg)](LICENSE)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Python Versions](https://img.shields.io/pypi/pyversions/{{cookiecutter.project_slug}})](https://pypi.org/project/{{cookiecutter.project_slug}})

{{cookiecutter.project_short_description}}

## Getting Started

### Prerequisites

- Python 3.10+
- Poetry

### Installation

1.  Clone the repository:
    ```sh
    git clone https://github.com/example/example.git
    cd my_python_project
    ```
2.  Install dependencies:
    ```sh
    poetry install
    ```

### Usage

-   Run the linter:
    ```sh
    poetry run pre-commit run --all-files
    ```
-   Run the tests:
    ```sh
    poetry run pytest
    ```
