def solution(n):
    
    temp = n + 1
    while True :
        if str(bin(n)).count('1') == str(bin(temp)).count('1') :
            return temp
        else :
            temp += 1
