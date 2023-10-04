from collections import deque

def solution(people, limit):
    people.sort()
    cnt = 0
    
    people = deque(people)
    
    while len(people) > 1: 
        if people[0] + people[-1] <= limit :
            people.pop()
            people.popleft()
            cnt += 1
        else :
            people.pop()
            cnt += 1
    
    if len(people) == 1 :
        cnt += 1
    
    return cnt