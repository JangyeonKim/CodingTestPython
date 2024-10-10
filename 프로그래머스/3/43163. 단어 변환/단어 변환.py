from collections import deque

def canTransform(word1, word2) :
    cnt = 0
    for w1, w2 in zip(word1, word2) :
        if w1 != w2 :
            cnt += 1
    return True if cnt == 1 else False

def bfs(queue, words, target) :
    answer = 0
    while queue :
        word, cnt = queue.popleft()
        if word == target :
            return cnt
        for wrd in words :
            if canTransform(word, wrd) :
                queue.append([wrd, cnt+1])
        

def solution(begin, target, words):
    if target not in words :
        return 0
    
    queue = deque([[begin, 0]])
    answer = bfs(queue, words, target)
        
    return answer