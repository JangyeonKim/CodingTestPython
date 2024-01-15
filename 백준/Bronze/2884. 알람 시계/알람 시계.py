hour, minu = map(int, input().split())

if minu < 45 :
    if hour == 0 :
        print(f"23 {minu+15}")
    else :
        print(f"{hour-1} {minu + 15}")
else :
    print(f"{hour} {minu-45}")