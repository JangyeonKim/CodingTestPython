
def solution(arr):
    answer = []
    
    for a in arr :
        while answer and answer[-1] == a :
            answer.pop()
        answer.append(a)

    return answer