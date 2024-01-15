in_list = []

for _ in range(3) :
    in_list.append(int(input()))

mul = 1
for i in range(3) :
    mul *= in_list[i]
    
dict = {}
for i in range(10) :
    dict[str(i)] = 0
    
for s in str(mul) :
    dict[s] += 1
    
for v in dict.values() :
    print(v)
