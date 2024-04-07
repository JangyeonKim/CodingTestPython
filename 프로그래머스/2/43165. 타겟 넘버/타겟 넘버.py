# 번호 하나 당 2개(+,-)로 2^len(numbers) 경우의 수 존재

# 1. bfs
def bfs_solution(numbers, target):
    ans_list = [0]
    
    for i in range(len(numbers)):
        temp = []
        for a in ans_list :
            temp.append(a+numbers[i])
            temp.append(a-numbers[i])
        ans_list = temp
            
    return ans_list.count(target)

# 2. dfs
def dfs(numbers, target, idx, value) :
    global cnt
    
    if idx == len(numbers) and value == target :
        cnt+=1
        return
    elif idx == len(numbers) :
        return
    
    dfs(numbers, target, idx+1, value + numbers[idx])
    dfs(numbers, target, idx+1, value - numbers[idx])

def solution(numbers, target):
    global cnt
    cnt = 0
    
    dfs(numbers, target, 0, 0)
    return cnt