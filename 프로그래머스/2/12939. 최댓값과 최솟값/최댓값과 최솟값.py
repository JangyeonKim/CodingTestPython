def solution(s):
    num_list = list(map(int, s.split()))
    num_list.sort()
    
    answer = f"{num_list[0]} {num_list[-1]}"
    
    return answer