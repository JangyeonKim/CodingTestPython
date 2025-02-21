import sys

note = "".join(list(sys.stdin.readline().strip().split()))

if note == "12345678" :
    print("ascending")
elif note == "87654321" :
    print("descending")
else :
    print("mixed")