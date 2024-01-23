def solution(n):
    answer = n
    cnt_1 = str(bin(n)).count("1")
    
    while True :
        answer += 1
        if str(bin(answer)).count("1") == cnt_1 :
            return answer
