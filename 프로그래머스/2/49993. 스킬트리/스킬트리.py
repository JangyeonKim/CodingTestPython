def solution(skill, skill_trees):
    ans_arr = []
    
    for candidate in skill_trees :
        arr = []
        for sk in candidate :
            if sk in skill :
                arr.append(sk)
        ans_arr.append("".join(arr))
    
    answer = 0
    for ans in ans_arr :
        if skill.startswith(ans) :
            answer += 1
            
    return answer
    