import sys

n = int(sys.stdin.readline().strip())

for _ in range(n) :
    H, W, N = map(int, sys.stdin.readline().strip().split())

    floor = N % H
    if floor == 0 :
        floor = H # 나누어떨어지면 꼭대기층
        
    step = (N - 1) // H + 1
    step_s = f"{step:02d}"
    
    print(str(floor) + step_s)