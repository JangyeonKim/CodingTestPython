def solution(nums):
    set_arr = len(set(nums))
    half_len = len(nums) / 2
    
    if set_arr >= half_len :
        return half_len
    else :
        return set_arr