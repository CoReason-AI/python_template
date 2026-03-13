#!/usr/bin/env python3
"""
Architecture Evaluation Gate.

This script enforces 'Passive by Design' boundaries by analyzing AST
for hidden kinetic execution side-effects outside designated structural components.
"""
import ast
import sys
from pathlib import Path


def evaluate_file(filepath: Path) -> list[str]:
    violations = []
    try:
        content = filepath.read_text(encoding="utf-8")
        tree = ast.parse(content, filename=str(filepath))
    except SyntaxError as e:
        return [f"Syntax error in {filepath}: {e}"]
    except Exception as e:
        return [f"Could not read {filepath}: {e}"]

    for node in ast.walk(tree):
        # Example naive check: block generic print() in production code outside cli/main.
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "print":
                if "cli" not in filepath.parts and "scripts" not in filepath.parts:
                    violations.append(f"Forbidden kinetic execution (print) found at line {node.lineno}")

    return violations


def main() -> None:
    src_dir = Path("src")
    if not src_dir.exists():
        print("No src directory found to evaluate.")
        sys.exit(0)

    all_violations = []
    for filepath in src_dir.rglob("*.py"):
        violations = evaluate_file(filepath)
        if violations:
            all_violations.append((filepath, violations))

    if all_violations:
        print("Architecture evaluation failed:")
        for filepath, violations in all_violations:
            print(f"  {filepath}:")
            for v in violations:
                print(f"    - {v}")
        sys.exit(1)
    else:
        print("Architecture evaluation passed.")


if __name__ == "__main__":
    main()
