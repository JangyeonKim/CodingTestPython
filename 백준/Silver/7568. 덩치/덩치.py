N = int(input())

arr = []

for _ in range(N) :
    h, w = map(int, input().split())
    arr.append([h, w])
    
for i in range(len(arr)) :
    temp_arr = arr[:]
    
    h, w = temp_arr.pop(i)
    cnt = 1
    
    for hh, ww in temp_arr :
        if hh > h and ww > w :
            cnt += 1
    
    print(cnt, end = " ")