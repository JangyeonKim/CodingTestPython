

def solution(storey):
    answer = 0
    
    while storey != 0 :
        storey, moves = storey//10, storey%10
        
        if moves > 5 or (moves == 5 and storey % 10 >= 5) : # 뒤의 조건 : 5이고 그 앞의 자리가 5 이상일 경우엔 이렇게 처리하는게 더 최소의 경우임 
            moves = 10 - moves
            storey += 1
        answer += moves
    
    return answer