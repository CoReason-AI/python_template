# Copyright (c) {{ cookiecutter.license_contributor }}
#
# This software is proprietary and dual-licensed.
# Licensed under the Prosperity Public License 3.0 (the "License").
# A copy of the license is available at https://prosperitylicense.com/versions/3.0.0
# For details, see the LICENSE file.
# Commercial use beyond a 30-day trial requires a separate license.
#
# Source Code: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

from {{ cookiecutter.project_slug }}.main import hello_world

def test_hello_world():
    assert hello_world() == "Hello World!"
