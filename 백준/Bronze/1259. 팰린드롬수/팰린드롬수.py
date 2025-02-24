while True :
    num = input()
    if num == '0' :
        break
    
    if len(num) % 2 == 0 :
        mid = len(num)//2
    else :
        mid = len(num) // 2 + 1
    
    if num[:mid] == num[-1:-mid-1:-1] :
        print("yes")
    else :
        print("no")