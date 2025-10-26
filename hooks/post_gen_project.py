#!/usr/bin/env python
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

if __name__ == '__main__':
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '-A'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit'])
    subprocess.call(['pip', 'install', '-e', '.[dev]'])
