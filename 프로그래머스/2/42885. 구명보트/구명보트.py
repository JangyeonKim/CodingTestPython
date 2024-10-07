from collections import deque
def solution(people, limit):
    answer = 0
    
    people.sort()
    people = deque(people)
    
    while people :
        pig = people.pop()
        if people and pig + people[0] <= limit :
            people.popleft()
        answer += 1
    
    return answer