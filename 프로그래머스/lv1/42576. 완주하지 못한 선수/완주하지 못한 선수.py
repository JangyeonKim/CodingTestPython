def solution(participant, completion):
    
#     for com in completion :
#         if com in participant :
#             participant.remove(com)
    
#     return participant[0]

    participant.sort()
    completion.sort ()
    
    for i in range(len(completion)) :
        if participant[i] != completion[i] :
            return participant[i]
        
    return participant[-1] # for문 다 돌면 마지막 사람이 완주 못한 사람