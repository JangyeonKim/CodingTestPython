iter = int(input())

for _ in range(iter) :
    n, s = input().split()
    ans = ""
    for ss in s :
        ans += ss * int(n)
    print(ans)