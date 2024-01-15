case = int(input())

for _ in range(case) :
    string = input()
    cnt = 0
    ans = []
    for s in string :
        if s == "O" :
            cnt += 1
            ans.append(cnt)
        else :
            cnt = 0
            ans.append(cnt)
    print(sum(ans))