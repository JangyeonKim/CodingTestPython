def solution(numbers):
    
    numbers.sort(key = lambda x : str(x)*3, reverse = True)
    
    answer = ''
    for num in numbers :
        answer += str(num)
    
    return str(int(answer))