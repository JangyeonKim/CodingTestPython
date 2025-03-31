N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 방향 - 0 : 북, 1: 동, 2 : 남, 3 : 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0

def robot(x, y, d, room):
    global cnt
    while True:
        if room[x][y] == 0:
            room[x][y] = -1
            cnt += 1

        moved = False
        for _ in range(4):
            d = (d + 3) % 4  # 반시계 방향 회전
            nx = x + dx[d] 
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
                x, y = nx, ny
                moved = True
                break

        if not moved: # 방향 유지하며 후진 가능 여부
            back_x = x - dx[d]
            back_y = y - dy[d]
            if 0 <= back_x < N and 0 <= back_y < M and room[back_x][back_y] != 1:
                x, y = back_x, back_y
            else: # 작동 멈춤
                return cnt

answer = robot(r, c, d, room)
print(answer)
