import sys
import os

cwd = os.getcwd()
print(cwd)

module_path = os.path.abspath(cwd + "\\...")
print(module_path)

print(__package__)


if __package__ is None:
    print("package is none...")
    import bs  
else:    
    import formula.bs

