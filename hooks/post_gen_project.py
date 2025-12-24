# Copyright (c) CoReason, Inc.
#
# This software is proprietary and dual-licensed.
# Licensed under the Prosperity Public License 3.0 (the "License").
# A copy of the license is available at https://prosperitylicense.com/versions/3.0.0
# For details, see the LICENSE file.
# Commercial use beyond a 30-day trial requires a separate license.
#
# Source Code: https://github.com/CoReason-AI/python_template

# This script is executed after the project is generated.

import subprocess
import os
import sys

print("Project generated successfully!")
print("Initializing Git repository...")

try:
    # On Windows, shell=True is required to resolve commands like 'poetry' if they are batch files
    # or not strictly executables. On POSIX, shell=False is preferred.
    use_shell = sys.platform == "win32"

    # Initialize git
    subprocess.run(["git", "init", "-b", "main"], check=True, shell=use_shell)
    subprocess.run(["git", "add", "."], check=True, shell=use_shell)
    subprocess.run(["git", "commit", "-m", "Initial commit from cookiecutter"], check=True, shell=use_shell)

    # Install dependencies
    print("\nInstalling dependencies with Poetry...")
    subprocess.run(["poetry", "install"], check=True, shell=use_shell)

    print("\nSuccessfully initialized git repo and installed dependencies.")
    print("Your new project is ready at:", os.getcwd())

except Exception as e:
    print(f"\nAn error occurred during post-generation setup: {e}")
    print("Please manually run 'git init' and 'poetry install'.")
