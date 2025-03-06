import sys
input = sys.stdin.readline

N, M = map(int, input().split())

no_watch = set()
no_heard = set()

for _ in range(N) :
    no_watch.add(input().strip())

for _ in range(M) :
    no_heard.add(input().strip())
    
intersection = no_watch.intersection(no_heard)
intersection = list(intersection)
intersection.sort()

print(len(intersection))
for i in intersection :
    print(i)