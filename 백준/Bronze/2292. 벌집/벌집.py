N = int(input())

# 1 (1) -> 6 (2~7) -> 12 (8~19) -> 18 (20~37) -> 24 (38~61) -> ...

if N == 1 :
    print(1)
    
else : 
    start = 2
    i = 1

    while True :
        end = start + (6 * i) - 1
        if N >= start and N <= end :
            break
        start = end + 1
        i += 1
    
    print(i+1)