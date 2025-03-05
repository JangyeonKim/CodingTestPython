import sys 

input = sys.stdin.readline

n = int(input())

# n=1 : 1
# n=2 : 3
# n=3 : 5
# n=4 : 11
# n=5 : 21

answer = [0] * (n+1)
answer[1] = 1

if n >= 2 :
    answer[2] = 3

    for i in range(3, n+1) :
        answer[i] = answer[i-2] *2 + answer[i-1]

print(answer[-1] % 10007)