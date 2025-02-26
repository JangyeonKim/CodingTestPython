N = int(input())

arr = []

for _ in range(N) :
    arr.append(list(map(int, input().split())))
    
arr.sort(key = lambda x : (x[1], x[0]))

for a, b in arr :
    print(a, b)