# Copyright (c) CoReason, Inc.
#
# This software is proprietary and dual-licensed.
# Licensed under the Prosperity Public License 3.0 (the "License").
# A copy of the license is available at https://prosperitylicense.com/versions/3.0.0
# For details, see the LICENSE file.
# Commercial use beyond a 30-day trial requires a separate license.
#
# Source Code: https://github.com/CoReason-AI/python_template

import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_slug }}'

if not re.match(MODULE_REGEX, module_name):
    print(f'ERROR: The project slug ({module_name}) is not a valid Python module name.')
    print('Please do not use a "-" and ensure it starts with a letter or underscore.')
    sys.exit(1)
