asc = [x for x in range(1,9)]
dsc = sorted(asc, reverse = True)

inp = list(map(int, input().split()))

if inp == asc :
    print("ascending")
elif inp == dsc :
    print("descending")
else :
    print("mixed")