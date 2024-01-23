import sys

def cal_yaksu(num) :
    yak_list = []
    for i in range(1, num+1) :
        if i**2 > num :
            break
        elif num % i == 0 :
            yak_list.append(i)
            yak_list.append(int(num/i))
    return sorted(yak_list)

a, b = map(int, sys.stdin.readline().strip().split())

a_yak = cal_yaksu(a)
b_yak = cal_yaksu(b)

max_yaksu = max(set(a_yak) & set(b_yak))
min_baesu = int(a * b / max_yaksu) # 최소공배수 : 두 수의 곱 / 최대공약수

print(max_yaksu)
print(min_baesu)
