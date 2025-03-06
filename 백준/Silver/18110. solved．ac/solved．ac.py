import sys
input = sys.stdin.readline

# 배운점
# round() 함수는 .5에 대해 가장 가까운 짝수로 반올림
# 0.5를 더하고 math.floor로 버림을 하자
from math import floor

n = int(input())
arr = []

for _ in range(n) :
    arr.append(int(input()))
arr.sort()
    
if not arr :
    print(0)
else :
    cut = floor((len(arr) * 0.15) + 0.5)
    cut_arr = arr[cut:len(arr)-cut]
    # print(cut_arr)
    if cut_arr : 
        print(floor((sum(cut_arr) / len(cut_arr) + 0.5)))
    else :
        print(0)