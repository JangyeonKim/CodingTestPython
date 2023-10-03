def solution(n, words):
    answer_list = [words[0]]
    cnt = 1
    
    for i in range(1, len(words)) :
        if words[i][0] != words[i-1][-1] :
            break
        else :
            if words[i] in answer_list :
                break
            else :
                answer_list.append(words[i])
                cnt += 1
    
    if cnt == len(words) :
        return [0, 0]
    else :
        cnt += 1 # 사람이 3명이고 cnt가 9이면, 3번째 사람이 3번째 말할 때 탈락
                 # 사람이 2명이고 cnt가 5이면, 1번째 사람이 3번재 말할 때 탈락
        if cnt % n == 0 :
            person = n
            turn = cnt // n
            
        else :
            person = cnt % n
            turn = cnt // n + 1
            
        return [person, turn]
        