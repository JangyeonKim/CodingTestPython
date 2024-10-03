from collections import deque

def count_diff(word1, word2) :
    cnt = 0
    for w1, w2 in zip(word1, word2) :
        if w1 != w2 :
            cnt += 1
            
    return True if cnt==1 else False

def bfs(begin, target, words, answer) :
    queue = deque([[begin, answer]])
    check = []
    
    while queue :
        word, answer = queue.popleft()
        if word == target :
            return answer
        for w in words :
            if w not in check and count_diff(word, w) :
                queue.append([w, answer+1])
                check.append(w)
    return 0
            
def solution(begin, target, words):
    if target not in words :
        return 0
    
    answer = bfs(begin, target, words, 0)
    
    return answer 