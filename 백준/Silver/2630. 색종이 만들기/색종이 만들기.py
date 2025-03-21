from collections import deque
N = int(input())

square = []
for _ in range(N) :
    square.append(list(map(int, input().split())))

cnt_W = cnt_B = 0

def isSquare(subgraph) :
    c = subgraph[0][0]
    for x in range(len(subgraph)) :
        for y in range(len(subgraph[0])) :
            if subgraph[x][y] != c :
                return False
    return True

subSquare = deque([square])

while subSquare: 
    sub = subSquare.popleft()
    if isSquare(sub):
        if sub[0][0] == 0 :
            cnt_W += 1
        else :
            cnt_B += 1

    else :
        div = len(sub) // 2

        new_sub1 = []
        new_sub2 = []
        new_sub3 = []
        new_sub4 = []
        for y in range(div) :
            new_sub1.append(sub[y][:div])
            new_sub2.append(sub[y][div:len(sub)])
        for y in range(div, len(sub)) :
            new_sub3.append(sub[y][:div])
            new_sub4.append(sub[y][div:len(sub)])

        subSquare.append(new_sub1)
        subSquare.append(new_sub2) 
        subSquare.append(new_sub3) 
        subSquare.append(new_sub4) 

print(cnt_W)
print(cnt_B)