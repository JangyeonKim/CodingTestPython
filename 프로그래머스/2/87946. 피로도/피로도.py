from itertools import permutations

def count(k, dg) :
    global answer
    cnt = 0
    for d in dg :
        if d[0] <= k :
            k -= d[1]
            cnt +=1
        else :
            break
    
    if cnt > answer :
        answer = cnt

def solution(k, dungeons):
    global answer
    answer = -1
    
    dungeon = [x for x in dungeons if x[0] <= k]
    
    d_list = list(permutations(dungeon, len(dungeon)))
    # print(d_list)
    
    for dg in d_list :
        count(k, dg)
    
    return answer