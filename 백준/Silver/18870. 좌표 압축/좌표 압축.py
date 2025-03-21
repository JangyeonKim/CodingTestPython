import sys
input= sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

aarr = sorted(set(arr))
dic = {aarr[i] : i for i in range(len(aarr))}
for a in arr :
    print(dic[a], end = " ")