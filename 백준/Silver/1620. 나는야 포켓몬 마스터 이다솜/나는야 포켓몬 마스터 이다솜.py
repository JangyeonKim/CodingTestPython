import sys
input = sys.stdin.readline

N, M = map(int, input().split())

poket_name = dict()
poket_num = dict()

for idx in range(1, N+1) :
    poket = input().strip()
    
    poket_name[poket] = idx
    poket_num[idx] = poket
    
for _ in range(M) :
    prob = input().strip()
    
    if prob.isalpha() :
        print(poket_name[prob])
    else :
        print(poket_num[int(prob)])