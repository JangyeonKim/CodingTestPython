def solution(nums):

    choice = len(nums)//2
    
    s1 = set(nums)
    
    if len(s1) < choice :
        return len(s1)
    else :
        return choice