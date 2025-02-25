import sys

input = sys.stdin.readline

T = int(input())

# 아래층의 1호부터 b호까지 사람들의 합만큼 데려와 살아야함
# 0층부터 있음. i호에는 i명 삼

for _ in range(T) :
    k = int(input()) # k 층
    n = int(input()) # n 호
    
    floor_arr = [x for x in range(1, n+1)] # 0층 init (1~n)
    for i in range(k) :
        temp_arr = [0] * n
        for j in range(n) :
            temp_arr[j] = sum(floor_arr[:j+1])
        floor_arr = temp_arr
    
    print(floor_arr[-1])
        