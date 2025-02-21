import sys

_ = sys.stdin.readline()

arr = list(map(int, sys.stdin.readline().strip().split()))
arr.sort()

print(f"{arr[0]} {arr[-1]}")