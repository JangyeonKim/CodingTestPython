n = int(input())

if n <= 2 :
    print(n)
else :
    arr = [0, 1, 2] + [0] * (n-2)
    
    for i in range(3, n+1) :
        arr[i] = arr[i-1] + arr[i-2]
        
    print(arr[-1] % 10007)