import sys

# 2층 : 1 4 10 20 ...
# 1층 : 1 3 6 10 ...
# 0층 : 1 2 3 4 ... n

def apart(k, n) :
    structure = [[0] * (n) for _ in range (k+1)]
    structure[0] = [x for x in range(1, n+1)]
    
    for kk in range(1, k+1) :
        structure[kk][0] = 1
        
        for nn in range(1,n) :
            structure[kk][nn] = sum(structure[kk-1][:nn+1])
    
    print(structure[-1][-1])

num_case = int(sys.stdin.readline().strip())

for _ in range(num_case) :
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    apart(k, n)
    