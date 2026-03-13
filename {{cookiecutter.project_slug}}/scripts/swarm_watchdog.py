#!/usr/bin/env python3
"""
Swarm Watchdog.

Enforces PPL 3.0 licensing in all relevant source files
and scans for epistemic contamination.
"""

import sys
from pathlib import Path

REQUIRED_LICENSE_SNIPPET = "Licensed under the Prosperity Public License 3.0"
CONTAMINATION_KEYWORDS = ["GPL", "AGPL", "copyleft", "CRUD", "Delete", "Create", "Update"]
ALLOWED_EXTENSIONS = {".py", ".md", ".toml", ".yaml", ".yml"}


def check_file_for_compliance(filepath: Path) -> list[str]:
    violations = []
    try:
        content = filepath.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []

    # Check for PPL 3.0 License if it's a primary source file
    if filepath.suffix == ".py" and REQUIRED_LICENSE_SNIPPET not in content and "tests/" not in str(filepath):
        violations.append("Missing PPL 3.0 License header.")

    # Check for Epistemic Contamination
    for keyword in CONTAMINATION_KEYWORDS:
        if keyword in content and "AGENTS.md" not in str(filepath) and "swarm_watchdog.py" not in str(filepath):
            violations.append(f"Contamination found: Keyword '{keyword}' is prohibited.")

    return violations


def main() -> None:
    src_dir = Path("src")
    if not src_dir.exists():
        print("No src directory found to watch.")
        sys.exit(0)

    all_violations = []
    for filepath in src_dir.rglob("*"):
        if filepath.is_file() and filepath.suffix in ALLOWED_EXTENSIONS:
            violations = check_file_for_compliance(filepath)
            if violations:
                all_violations.append((filepath, violations))

    if all_violations:
        print("Swarm watchdog found violations:")
        for filepath, violations in all_violations:
            print(f"  {filepath}:")
            for v in violations:
                print(f"    - {v}")
        sys.exit(1)
    else:
        print("Swarm watchdog validation passed.")


if __name__ == "__main__":
    main()
