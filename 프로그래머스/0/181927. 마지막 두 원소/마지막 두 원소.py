def solution(num_list):
    a = num_list[-1]
    b = num_list[-2]
    
    if a > b :
        num_list.append(a-b)
    else :
        num_list.append(a*2)
    return num_list