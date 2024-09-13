def solution(people, limit):
    boats = 0  # 필요한 구명보트의 수
    
    people.sort(reverse=True)
    
    i= 0 
    j = len(people)-1
    
    while i <= j :
        # print(i, j)
        if people[i] + people[j] <= limit :
            i+=1
            j-=1
            boats += 1
        else :
            i+=1
            boats += 1

    return boats