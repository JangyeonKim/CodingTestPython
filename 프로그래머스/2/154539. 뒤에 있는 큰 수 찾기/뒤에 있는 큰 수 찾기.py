def solution(numbers):
    answer = [0] * len(numbers)
    
    stack = []
    for i in range(len(numbers)) :
        while stack and numbers[stack[-1]] < numbers[i] : # 오큰수 발견
            answer[stack.pop()] = numbers[i] # 오큰수 할당
        
        stack.append(i) # 오큰수 할당 대기
        
    while stack : # 오큰수 없는 자리에 -1 할당
        answer[stack.pop()] = -1
    
    return answer