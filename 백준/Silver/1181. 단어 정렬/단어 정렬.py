N = int(input())

arr = []
for _ in range(N) :
    a = input()
    if a not in arr :
        arr.append(a)

arr.sort(key = lambda x : (len(x), x))

while arr :
    print(arr.pop(0))