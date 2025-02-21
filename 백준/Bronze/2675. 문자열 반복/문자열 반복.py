import sys

n = int(sys.stdin.readline().strip())
for _ in range(n) :
    iteration, string = sys.stdin.readline().strip().split()
    
    ans = ""
    for s in string :
        ans += s*int(iteration)
    
    print(ans)