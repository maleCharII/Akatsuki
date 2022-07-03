import sys
from pathlib import Path

print('='*70)

print("finding path of current file")
file_path = Path(__file__)
print(file_path) # cast to string in class msg
print(type(file_path)) # it is an object

print('-'*70)

print("finding path of parent")
print(file_path.parent.absolute())
par_dir = Path(file_path.parent.absolute())
ROOT_DIR = par_dir.parent.absolute()
print(ROOT_DIR)

print('-'*70)

print("hacking the sys path...(temp effect)")
sys.path.insert(0, ROOT_DIR)

for d in sys.path:
    print(d)

print('='*70)