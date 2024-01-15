count = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

print(f"{num_list[0]} {num_list[-1]}")