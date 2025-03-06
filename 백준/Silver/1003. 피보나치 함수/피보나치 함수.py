import sys
input = sys.stdin.readline

# def fibo(n) :
#     global cnt0
#     global cnt1
    
#     if n == 0 :
#         cnt0+=1
#         return 0
#     elif n == 1 :
#         cnt1 +=1
#         return 1
#     else :
#         return fibo(n-1) + fibo(n-2)

T = int(input())
for _ in range(T) :
    n = int(input())
    
    cnt0 = [1, 0]
    cnt1 = [0, 1]

    if n < 2 :
        print(cnt0[n], cnt1[n])
    else :
        cnt0 += [0] * (n-1) 
        cnt1 += [0] * (n-1) 

        for i in range(2, n+1) :
            cnt0[i] = cnt0[i-1] + cnt0[i-2]
            cnt1[i] = cnt1[i-1] + cnt1[i-2]

        print(cnt0[-1], cnt1[-1])