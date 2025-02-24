N = input()

ans_list = []

for i in range(1, int(N)) :
    str_i = str(i)
    
    temp = i
    for s in str_i :
        temp += int(s)
    
    if temp == int(N) :
        ans_list.append(i)
        break
        
print(ans_list[0] if ans_list else 0)

    