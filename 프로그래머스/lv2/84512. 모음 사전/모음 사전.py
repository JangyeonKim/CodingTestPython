from itertools import product # 중복순열

def solution(word):
    
    alpha = ['A', 'E', "I", 'O', 'U']
    
    pd_list = []
    
    for i in range(1,6) :
        pd = list(product(alpha, repeat = i))
        for p in pd :
            pd_list.append("".join(p))
    
    pd_list.sort()
    
    ans = pd_list.index(word) + 1 # index 값 + 1 = 위치
    
    return ans