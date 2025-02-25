N = int(input())

# 정확하게 N을 만들 수 없으면 -1 출력

k_5 = N // 5
N -= 5 * k_5
k_3 = 0

while True :
    if N % 3 == 0 :
        k_3 = N//3
        print(k_5 + k_3)
        break
    else :
        if k_5 > 0 :
            k_5 -= 1
            N += 5
        else :
            print(-1)
            break
            