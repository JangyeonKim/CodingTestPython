def solution(n):
    answer = 0
    strn = str(bin(n))[2:]
    num1 = strn.count("1")
    
    while True :
        n += 1
        strnp = str(bin(n))[2:]
        num2 = strnp.count("1")

        if num1 == num2 :
            return n
