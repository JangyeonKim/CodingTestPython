def solution(s):
    s_list = s.lower().split(" ")
    # print(s_list)
    
    answer=[]
    for string in s_list :
        if string == "" or string[0].isdigit():
            answer.append(string)
        elif string[0].isalpha() :
            answer.append(string[0].upper() + string[1:])
    
    
    return " ".join(answer)