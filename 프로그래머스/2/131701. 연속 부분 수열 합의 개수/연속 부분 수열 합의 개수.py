def solution(elements):
    ans_list = []
    
    for win_len in range(1,len(elements)+1) : # 1~len(elements)
        if win_len == 1 :
            ans_list.append(elements)
        elif win_len == len(elements) :
            ans_list.append([sum(elements)])
        else :
            ele = elements[-(win_len-1):] + elements
            temp = []

            for i in range(len(elements)) :
                t = sum(ele[i:i+win_len])
                temp.append(t)
            ans_list.append(temp)
    
    ans = ans_list.pop()
    for a in ans_list :
        ans += a
    return len(set(ans))