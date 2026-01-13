# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

[![CI/CD](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/ci-cd.yml)
[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![License](https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/blob/main/LICENSE)
[![Codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
[![Downloads](https://static.pepy.tech/badge/{{ cookiecutter.project_slug }})](https://pepy.tech/project/{{ cookiecutter.project_slug }})
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

## Getting Started

### Prerequisites

- Python 3.12+
- Poetry

### Installation

1.  Clone the repository:
    ```sh
    git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
    cd {{ cookiecutter.project_slug }}
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
