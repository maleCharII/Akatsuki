import time
import sys

print("="*70)

n = 1000
arr = [ '|', '/', '-', '|', '\\']

for i in range(n):
    c = arr[i % len(arr)]
    d = arr[(i-1) % len(arr)]
    time.sleep(0.05)
    print(f">> let's wait ... {c} {d}\r", end=" ", flush=True)

print()
print("="*70)