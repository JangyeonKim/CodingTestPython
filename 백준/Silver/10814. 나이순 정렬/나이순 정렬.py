from collections import defaultdict

N = int(input())

d = defaultdict(list)

for _ in range(N) : 
    age, name = input().split()
    
    d[int(age)].append(name)
    
dd = sorted(d.items())

for a, n_arr in dd :
    for i in range(len(n_arr)) :
        print(a, n_arr[i])