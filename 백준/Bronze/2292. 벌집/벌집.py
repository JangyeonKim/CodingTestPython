import sys

num = int(sys.stdin.readline().strip())

if num == 1:
    print("1")
else : 
    ans = [1]
    n = 0
    while True :
        temp_ans = ans[n] + (n+1)*6
        ans.append(temp_ans)
    
        if temp_ans >= num :
            break
        n+=1
    
    print(len(ans))