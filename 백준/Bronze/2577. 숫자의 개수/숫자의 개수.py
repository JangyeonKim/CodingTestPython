import sys

num_dict = {}
for i in range(10) :
    num_dict[str(i)] = 0
    
num = 1
for _ in range(3) :
    num *= int(sys.stdin.readline().strip())

for s in str(num) :
    num_dict[s] += 1
    
for i in range(10) :
    print(num_dict[str(i)])