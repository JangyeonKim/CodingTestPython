upper_input = input().upper()

str_dict = {}

for s in upper_input :
    if s not in str_dict.keys() :
        str_dict[s] = 1
    else :
        str_dict[s] += 1
        
max_value = max(str_dict.values())
max_key = [k for k, v in str_dict.items() if v == max_value]

if len(max_key) > 1 :
    print("?")
else :
    print(max_key[0])