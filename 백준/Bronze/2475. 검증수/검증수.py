num = list(map(int, input().split()))
num = [x ** 2 for x in num]

print(sum(num) % 10)