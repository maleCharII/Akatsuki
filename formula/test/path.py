import sys
import os

cwd = os.getcwd()
print(cwd)

module_path = os.path.abspath(cwd + "\\...")
print(module_path)

print(__package__)

from .. import bs

