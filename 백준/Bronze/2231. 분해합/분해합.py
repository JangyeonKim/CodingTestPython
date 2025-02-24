N = int(input())

#ans_list = []
#
#for i in range(1, int(N)) :
#    str_i = str(i)
#    
#    temp = i
#    for s in str_i :
#        temp += int(s)
#    
#    if temp == int(N) :
#        ans_list.append(i)
#        break
#        
#print(ans_list[0] if ans_list else 0)

ans = 0

start = max(1, N - 9 * len(str(N))) # 탐색 범위 줄임

for i in range(start, N) :
    temp = i
    
    for s in str(i) :
        temp += int(s)
    
    if temp == N :
        ans = i
        break
print(ans)