def solution(s):
    answer = []
    
    s_list = s.split(" ")

    for s in s_list :
        answer.append(s.capitalize())
    
    return " ".join(answer)
 