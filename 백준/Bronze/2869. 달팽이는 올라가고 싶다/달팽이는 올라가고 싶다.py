A, B, V = map(int, input().split())

# x = day
# 올라가는 횟수 : x, 내려오는 횟수 : x-1
# V = Ax - B(x-1) --> x = (V-B)/(A-B)

day = (V-B) / (A-B)

if int(day) == day :
    print(int(day))
else :
    print(int(day)+1)