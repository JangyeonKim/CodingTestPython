count = int(input())
in_list = list(map(int, input().split()))

ans = []

for i in in_list :
    if i == 1 :
        pass
    elif i == 2 :
        ans.append(i)
    elif i == 3 :
        ans.append(i)
    else :
        cnt = 0
        for j in range(2, i) :
            if i % j == 0 :
                cnt += 1
                break
        if cnt == 0 :
            ans.append(i)

print(len(ans))
            