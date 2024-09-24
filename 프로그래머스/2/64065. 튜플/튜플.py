def solution(s):   
    s = s.replace("{", "").replace("}", "").split(",")
    ans = {}
    for ss in s :
        if int(ss) not in ans.keys() :
            ans[int(ss)] = 1
        else :
            ans[int(ss)] += 1
    
    answer = sorted(ans, key = lambda x : ans[x], reverse = True)
    
    return answer