def solution(nums):
    max_len = len(nums) / 2
    set_nums = set(nums)
    
    if len(set_nums) >= max_len :
        return max_len
    else :
        return len(set_nums)
    