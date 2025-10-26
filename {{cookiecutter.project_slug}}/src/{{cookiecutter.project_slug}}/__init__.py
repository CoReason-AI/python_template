# Copyright (c) {{ cookiecutter.copyright_year }} {{ cookiecutter.license_contributor }}
#
# This software is proprietary and dual-licensed.
# Licensed under the Prosperity Public License 3.0 (the "License").
# A copy of the license is available at https://prosperitylicense.com/versions/3.0.0
# For details, see the LICENSE file.
# Commercial use beyond a 30-day trial requires a separate license.
#
# Source Code: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

"""
{{ cookiecutter.project_short_description }}
"""

__version__ = "0.1.0"
__author__ = "{{ cookiecutter.author_name }}"
__email__ = "{{ cookiecutter.author_email }}"

from .main import hello_world

__all__ = ["hello_world"]
