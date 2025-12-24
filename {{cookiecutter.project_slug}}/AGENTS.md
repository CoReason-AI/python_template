# **AGENTS.md**

**Note to Agent:** This file contains strict rules and context for this repository. Read this before planning or executing tasks.

## **1\. Project Overview**

* **Type:** Python Application / Library
* **Language:** Python 3.12+ (Strict dependency)
* **Package Manager:** Poetry
* **License:** Prosperity Public License 3.0 (Proprietary/Dual-licensed)
* **Project Structure:** src layout (source code resides in src/{{ cookiecutter.project_slug }})

## **2\. Environment & Commands**

The project is managed via Poetry. Do not use pip directly unless inside a Docker build stage.

* **Install Dependencies:** poetry install
* **Run Linter (Pre-commit):** poetry run pre-commit run \--all-files
* **Run Tests:** poetry run pytest
* **Build Docs:** poetry run mkdocs build \--strict
* **Build Package:** poetry build (or python \-m build in CI)

## **3\. Development Rules**

### **Code Style & Quality**

This project uses **Ruff** for Python linting/formatting, **Mypy** for typing, and **Hadolint** for Dockerfiles.

* **Formatting:** Do not manually format. Run poetry run ruff format .
* **Linting:** Fix violations automatically where possible: poetry run ruff check \--fix .
* **Docker Linting:** Checked via pre-commit (hadolint).
* **Typing:**
  * Strict static typing is encouraged.
  * Run checks with: poetry run mypy .
  * Avoid Any wherever possible.
* **Logging:** Use loguru instead of the standard logging module.
  * *Good:* from loguru import logger \-\> logger.info("...")

### **File Structure**

* **Source Code:** src/{{ cookiecutter.project_slug }}/
  * main.py: Entry point.
  * \_\_init\_\_.py: Package definition.
* **Tests:** tests/
  * Test files must start with test\_.
  * Use pytest fixtures where appropriate.

### **Testing Guidelines**

**Mandatory Requirement: 100% Test Coverage.**

* **Test Strategy (Redundancy & Depth):**
  * **Redundant Coverage:** Verify critical logic via multiple vectors (e.g., unit tests for isolation AND integration tests for workflow). Overlap is desired.
  * **Simple Tests:** Verify happy paths and basic functionality.
  * **Complex Tests:** Verify multi-step workflows, state mutations, and heavy computation.
  * **Edge Cases:** Explicitly test boundary values, empty inputs, null states, and error handling.
  * **Exclusions:** Use \# pragma: no cover sparingly and **only** for defensive code that is unreachable in standard execution.
* **External Services & APIs:**
  * **Scenario A (Default):** Use mocks (unittest.mock, pytest-mock, or respx) for ALL external calls.
  * **Scenario B (Credentials Provided):** If the user provides API keys or connection strings:
    * **DO NOT** remove the mocks.
    * **ADD** a separate suite of live integration tests marked with @pytest.mark.live.
    * **Standard Env Vars:** Expect Postgres credentials in PGHOST, PGPORT, PGUSER, PGPASSWORD, PGDATABASE.
* **Safety:** Never hardcode credentials in tests. Use environment variables.

## **4\. Architecture & Security**

### **CI/CD Context**

* **CI Environment:** GitHub Actions (Matrix testing on Ubuntu, Windows, MacOS).
* **Python Versions:** Tests run against Python 3.12, 3.13, and 3.14.

### **Docker Strategy**

* **Multi-stage Build:** The Dockerfile has a builder stage and a runtime stage.
* **User:** The app runs as a non-root user (appuser). **DO NOT** change this to root.
* **Base Image:** Uses python:3.12-slim.

### **Dependencies**

* **Management:** Always add dependencies via poetry add \<package\>.
* **Lock File:** poetry.lock must be committed.
* **Vulnerability Scanning:** CI uses Trivy. Ensure no Critical/High vulnerabilities are introduced.

## **5\. Documentation**

* Documentation is built with **MkDocs Material**.
* Update docs/index.md or add new markdown files in docs/ when adding features.
* Ensure all public functions have docstrings (Google or NumPy style).
