def solution(s):
    remove_zero, cnt = 0, 0
    
    
    while s != "1" :
        lens_bef = len(s)
        # print(f"before : {s}")
        s = s.replace("0", "")
        # print(f"after : {s}")
        lens_aft = len(s)
        ans = lens_bef - lens_aft
        remove_zero += ans
        s = str(bin(lens_aft))[2:]
        # print(f"bin : {s}")
        cnt += 1
    
    return [cnt, remove_zero]