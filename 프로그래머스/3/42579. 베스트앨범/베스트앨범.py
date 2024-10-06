def solution(genres, plays):
    answer = []
    
    album = dict()
    
    for idx, (g, p) in enumerate(zip(genres, plays)) :
        if g not in album.keys() :
            album[g] = [p, [p,idx]]
        else :
            album[g].append([p,idx])
            album[g][0] += p
    
    album = [x for x in album.values()]
    album.sort(key = lambda x : x[0])

    
    while album : 
        al = album.pop()
        al.pop(0)
        
        al.sort(key = lambda x : [x[0], -x[1]])
        cnt = 0
        while al :
            answer.append(al.pop()[1])
            cnt += 1
            if cnt == 2:
                break
    
    return answer