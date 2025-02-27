N = int(input())

start = 666
cnt = 0

while True :
    if "666" in str(start) :
        cnt += 1
    
    if cnt == N :
        break
    
    start += 1

print(start)