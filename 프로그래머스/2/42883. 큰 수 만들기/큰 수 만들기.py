def solution(number, k):
    # 큰 수들만 남기자
    stack = []
    
    for num in number :
        while stack and stack[-1] < num and k > 0 :
            stack.pop()
            k -= 1
        stack.append(num)
        
    if k > 0 :
        stack = stack[:-k]
    
    return "".join(stack)