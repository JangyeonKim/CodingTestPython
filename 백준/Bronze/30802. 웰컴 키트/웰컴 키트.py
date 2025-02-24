import sys

N = int(sys.stdin.readline().strip()) # 23
T_list = list(map(int, sys.stdin.readline().strip().split())) # 3, 1, 4, 1, 5, 9
T, P = map(int, sys.stdin.readline().strip().split()) # 5, 7

order_T = [0 for _ in range(len(T_list))]

for idx, t in enumerate(T_list) :
    if t == 0 :
        pass
    else :
        a = t // T
        b = t % T
        if b != 0 :
            a += 1
        
        order_T[idx] = a
        
print(sum(order_T))
print(N//P, N%P)