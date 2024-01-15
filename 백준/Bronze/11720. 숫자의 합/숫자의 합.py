import sys

count = sys.stdin.readline().strip()
num = sys.stdin.readline().strip()

result = 0
for n in num :
    result += int(n)
    
print(result)