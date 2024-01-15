input_list = []
for _ in range(10) :
    input_list.append(int(input()) % 42)

print(len(set(input_list)))