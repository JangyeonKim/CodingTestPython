N = int(input())

arr = []
for i in range(N) :
    age, name = input().split()
    arr.append([int(age), i, name])
    
arr.sort(key = lambda x : (x[0], x[1]))

for a, i, n in arr :
    print(a, n)
