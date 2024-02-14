def solution(numbers):
    str_numbers = list(map(str, numbers))
    
    str_numbers.sort(reverse = True, key = lambda x : x*3)
    
    ans = '' 
    
    for s in str_numbers :
        ans += s
    
    return str(int(ans))