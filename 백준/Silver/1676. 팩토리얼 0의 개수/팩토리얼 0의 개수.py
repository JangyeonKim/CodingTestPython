n = int(input())
ans = 1

for i in range(1, n+1) :
    ans *= i
    
ans = str(ans)

cnt = 0
for j in range(-1, -len(ans)-1, -1) :
    if ans[j] == '0' :
        cnt += 1
    else :
        break
        
print(cnt)