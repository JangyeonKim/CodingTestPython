num_list = []

for _ in range(9) :
    num_list.append(int(input()))
    
idx_num_list = sorted([(num, idx) for (idx, num) in enumerate(num_list)])

print(idx_num_list[-1][0])
print(idx_num_list[-1][1]+1)