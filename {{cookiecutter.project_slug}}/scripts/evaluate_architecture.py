#!/usr/bin/env python3
"""
Architecture Evaluation Gate.

This script enforces 'Passive by Design' boundaries by analyzing AST
for hidden kinetic execution side-effects outside designated structural components.
"""
import ast
import re
import sys
from collections import defaultdict
from pathlib import Path


def parse_diff(diff_text: str) -> dict[Path, set[int]]:
    """
    Parses a unified diff and returns a mapping of changed files
    to a set of newly added or modified line numbers.
    """
    changes: dict[Path, set[int]] = defaultdict(set)
    current_file: Path | None = None
    current_line = 0

    for line in diff_text.splitlines():
        if line.startswith("+++ b/"):
            filepath = line[6:]
            current_file = Path(filepath)
        elif line.startswith("@@"):
            # e.g., @@ -1,4 +1,5 @@
            match = re.search(r"@@ -[0-9]+(?:,[0-9]+)? \+([0-9]+)(?:,[0-9]+)? @@", line)
            if match:
                current_line = int(match.group(1))
        elif current_file is not None:
            if line.startswith("+") and not line.startswith("+++"):
                changes[current_file].add(current_line)
                current_line += 1
            elif line.startswith(" ") or line.startswith("-"):
                if not line.startswith("-"):
                    current_line += 1
            # Note: We skip decrementing or incrementing for lines starting with '-'
            # as they are not in the new file version.

    return dict(changes)


def evaluate_file(filepath: Path, changed_lines: set[int] | None = None) -> list[str]:
    violations = []
    try:
        content = filepath.read_text(encoding="utf-8")
        tree = ast.parse(content, filename=str(filepath))
    except SyntaxError as e:
        return [f"Syntax error in {filepath}: {e}"]
    except Exception as e:
        return [f"Could not read {filepath}: {e}"]

    for node in ast.walk(tree):
        if not hasattr(node, "lineno"):
            continue

        # If we are given changed_lines, only check nodes on those lines.
        if changed_lines is not None and node.lineno not in changed_lines:
            continue

        # Example naive check: block generic print() in production code outside cli/main.
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "print":
                if "cli" not in filepath.parts and "scripts" not in filepath.parts:
                    violations.append(f"Forbidden kinetic execution (print) found at line {node.lineno}")

    return violations


def main() -> None:
    src_dir = Path("src")
    all_violations = []

    # Check if data is piped into stdin
    if not sys.stdin.isatty():
        diff_text = sys.stdin.read()
        if diff_text.strip():
            changed_files_map = parse_diff(diff_text)
            for filepath, changed_lines in changed_files_map.items():
                if filepath.suffix == ".py" and src_dir in filepath.parents and filepath.exists():
                    violations = evaluate_file(filepath, changed_lines)
                    if violations:
                        all_violations.append((filepath, violations))

            if all_violations:
                print("Architecture evaluation failed on PR diff:")
                for filepath, violations in all_violations:
                    print(f"  {filepath}:")
                    for v in violations:
                        print(f"    - {v}")
                sys.exit(1)
            else:
                print("Architecture evaluation passed on PR diff.")
                sys.exit(0)

    # Fallback: analyze all files in src/ if no diff is provided
    if not src_dir.exists():
        print("No src directory found to evaluate.")
        sys.exit(0)

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
