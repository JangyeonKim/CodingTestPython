def solution(genres, plays):
    answer = []
    play_dict = dict()
    
    for idx, (g, p) in enumerate(zip(genres, plays)) :
        if g not in play_dict.keys() :
            play_dict[g] = [p, [p, idx]]
        else :
            play_dict[g][0] += p
            play_dict[g].append([p, idx])       
    
    play_list = [x for x in play_dict.values()]
    play_list.sort(key = lambda x : x[0], reverse = True)
    
    for play in play_list :
        play.pop(0)
        play.sort(key = lambda x : [x[0], -x[1]], reverse = True)
        
        cnt = 0
        for p in play :
            answer.append(p[1])
            cnt += 1
            if cnt == 2 :
                break
                
    return answer
