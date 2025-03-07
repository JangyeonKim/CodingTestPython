import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pwd = dict()

for _ in range(N) :
    site, pw = input().strip().split()
    pwd[site] = pw

for _ in range(M) :
    print(pwd[input().strip()])