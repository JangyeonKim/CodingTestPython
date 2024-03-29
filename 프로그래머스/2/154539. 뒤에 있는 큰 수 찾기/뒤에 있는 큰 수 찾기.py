# stack을 이용한 풀이
# queue를 사용해서 2중 반복문으로 작성하였을 경우 시간 초과
def solution(numbers):
    answer = [0] * len(numbers)
    stack = []
    
    # 1. for문 : 뒤에있는 큰 수가 있는 경우에 대한 처리
    for i in range(len(numbers)) :
        while stack and numbers[stack[-1]] < numbers[i] :# stack[-1] 인덱스에 해당하는 numbers의 수보다 numbers[i]가 더 크면. 즉, 뒷큰수이면 
            answer[stack.pop()] = numbers[i] # 해당 index에 대해 뒷큰수 할당
        stack.append(i)
    
    # 2. while문 : 남은 부분들에 대해 -1 처리
    while stack :
        answer[stack.pop()] = -1
        
    return answer