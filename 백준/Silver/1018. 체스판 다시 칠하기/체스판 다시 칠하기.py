import sys
input = sys.stdin.readline

bw = ['B', 'W'] * 4
wb = ['W', 'B'] * 4

chess = [[] for _ in range(8)]

chess_bw = chess[:]
for b in range(0, 8, 2) :
    chess_bw[b] = bw
for w in range(1, 9, 2) :
    chess_bw[w] = wb

chess_wb = chess[:]
for w in range(0, 8, 2) :
    chess_wb[w] = wb
for b in range(1, 9, 2) :
    chess_wb[b] = bw

def detect(candidate, chess_bw, chess_wb) :
    cnt_bw = cnt_wb = 0
    
    for i in range(8) :
        for j in range(8) :
            # bw case
            if candidate[i][j] != chess_bw[i][j] :
                cnt_bw += 1
            # wb case    
            if candidate[i][j] != chess_wb[i][j] :
                cnt_wb += 1

    return min(cnt_bw, cnt_wb)

N, M = map(int, input().split())
arr = []
for _ in range(N) : 
    arr.append(list(input().strip()))

n_range = N-8+1
m_range = M-8+1

s = 0
e = 8

answer = []

for n in range(n_range) :
    for m in range(m_range) :
        arr_c = [a[s+m : e+m] for a in arr[s+n : e+n]]

        answer.append(detect(arr_c, chess_bw, chess_wb))

print(min(answer))