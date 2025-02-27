from collections import deque

N, K = map(int, input().split())

arr = [x for x in range(1, N+1)]

queue = deque(arr)

answer = []

while queue :
    cnt = 0

    for _ in range(K-1) :
        queue.append(queue.popleft())

    answer.append(str(queue.popleft()))

ans = "<"
ans += ", ".join(answer)
ans += ">"

print(ans)