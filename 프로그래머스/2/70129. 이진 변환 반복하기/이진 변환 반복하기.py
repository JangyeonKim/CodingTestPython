def transformation(x) :
    temp_len = len(x)
    
    no_zero_x = ''
    for xx in x :
        if xx == "1" :
            no_zero_x += xx
    
    zero_cnt = temp_len - len(no_zero_x)

    bin_x = str(bin(len(no_zero_x)))[2:]
    
    return bin_x, zero_cnt

def solution(s) :
    tr_result, temp_zero_cnt = transformation(s)
    zero_cnt = temp_zero_cnt

    cnt=1
    
    if tr_result == "1" :
        return [cnt, zero_cnt]
    
    while True :
        tr_result, temp_zero_cnt = transformation(tr_result)
        cnt+=1
        zero_cnt += temp_zero_cnt
        
        if tr_result == "1" :
            break
    
    return [cnt, zero_cnt]