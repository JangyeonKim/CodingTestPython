# def solution(s):
#     answer = s

#     while "()" in answer :
#         answer = answer.replace("()", "")

    
#     if answer == "" :
#         return True
#     else :
#         return False

def solution(s) :
    stack = []
    for c in s : 
        if c == "(" :
            stack.append(c)
        else : # c == ")"
            if stack : # 스택에 원소가 남아있는 경우
                stack.pop()
            else : # 짝이 안맞음
                return False
    
    # for문 종료 후 stack 비어있는지 확인
    if stack :
        return False
    else :
        return True
                