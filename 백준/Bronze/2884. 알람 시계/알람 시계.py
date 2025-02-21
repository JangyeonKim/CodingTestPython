import sys

H, M = map(int, sys.stdin.readline().strip().split())

if M < 45 :
    H -= 1
    M = 60 - (45-M)
    if H < 0 :
        H += 24
else :
    M -= 45
    
print(f"{H} {M}")