N, M = map(int, input().split())

num_list = list(map(int, input().split()))

#ans = []

#for i in range(len(num_list)) :
#    temp_list = num_list[:]
#    temp_M = M - temp_list.pop(i)
#    
#    for j in range(len(temp_list)) :
#        ttemp_list = temp_list[:]
#        ttemp_M = temp_M - ttemp_list.pop(j)
#        
#        for tt in ttemp_list :
#            candidate = ttemp_M - tt
#            
#            if candidate >= 0 :
#                ans.append(M-candidate)
#                
# ans.sort()
# print(ans[-1])

ans = 0
for i in range(N-2) :
    for j in range(i+1, N-1) :
        for k in range(j+1, N) :
            val = num_list[i] + num_list[j] + num_list[k]
            
            if val <= M and val > ans :
                ans = val
print(ans)
