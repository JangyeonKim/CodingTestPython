def solution(s):
    cnt_zero = 0
    cnt_transform = 0
    cnt = 0
    while True :
        cnt_zero += s.count('0')
        s = s.replace('0', "")
        
        length = len(s)
        binary = bin(length)[2:]

        s = str(binary)
        cnt_transform += 1

        if s == "1" :
            break
        
    return [cnt_transform, cnt_zero]
        
    