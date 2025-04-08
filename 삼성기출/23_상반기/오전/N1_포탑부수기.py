'''
https://www.codetree.ai/ko/frequent-problems/problems/destroy-the-turret/description
'''

from collections import deque

# 입력
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
atk_time = [[0] * M for _ in range(N)]

# 방향: 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def choice_attacker():
    min_power = 5001
    ax = ay = -1

    for x in range(N):
        for y in range(M):
            if arr[x][y] != 0:
                if arr[x][y] < min_power:
                    min_power = arr[x][y]
                    ax, ay = x, y
                elif arr[x][y] == min_power:
                    if atk_time[x][y] > atk_time[ax][ay]:
                        ax, ay = x, y
                    elif atk_time[x][y] == atk_time[ax][ay]:
                        if x + y > ax + ay:
                            ax, ay = x, y
                        elif x + y == ax + ay:
                            if y > ay:
                                ax, ay = x, y
    return ax, ay

def choice_target(ax, ay):
    max_power = -1
    tx = ty = -1

    for x in range(N):
        for y in range(M):
            if arr[x][y] != 0 and (x != ax or y != ay):
                if arr[x][y] > max_power:
                    max_power = arr[x][y]
                    tx, ty = x, y
                elif arr[x][y] == max_power:
                    if atk_time[x][y] < atk_time[tx][ty]:
                        tx, ty = x, y
                    elif atk_time[x][y] == atk_time[tx][ty]:
                        if x + y < tx + ty:
                            tx, ty = x, y
                        elif x + y == tx + ty:
                            if y < ty:
                                tx, ty = x, y
    return tx, ty

def laser_atk(ax, ay, tx, ty, shoot):
    queue = deque()
    queue.append((ax, ay, []))
    visited = [[False]*M for _ in range(N)]
    visited[ax][ay] = True

    while queue:
        x, y, path = queue.popleft()
        if x == tx and y == ty:
            arr[tx][ty] -= shoot
            atk[tx][ty] = False
            for rx, ry in path:
                if (rx, ry) != (ax, ay) and (rx, ry) != (tx, ty):
                    arr[rx][ry] -= shoot // 2
                    atk[rx][ry] = False
            return True

        for d in range(4):
            nx = (x + dx[d]) % N
            ny = (y + dy[d]) % M
            if not visited[nx][ny] and arr[nx][ny] > 0:
                visited[nx][ny] = True
                queue.append((nx, ny, path + [(nx, ny)]))
    return False

def bomb_atk(ax, ay, tx, ty, shoot):
    arr[tx][ty] -= shoot
    atk[tx][ty] = False
    ddx = dx + [-1, -1, 1, 1]
    ddy = dy + [-1, 1, -1, 1]

    for i in range(8):
        nx = (tx + ddx[i]) % N
        ny = (ty + ddy[i]) % M
        if (nx, ny) != (ax, ay) and arr[nx][ny] > 0:
            arr[nx][ny] -= shoot // 2
            atk[nx][ny] = False

def break_check():
    for i in range(N):
        for j in range(M):
            if arr[i][j] < 0:
                arr[i][j] = 0

def max_check():
    return max(map(max, arr))

def turret_check():
    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                count += 1

    if count == 1:
        print(max_check())
        exit()

    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and atk[i][j]:
                arr[i][j] += 1

# 메인 루프
time = 1
for _ in range(K):
    atk = [[True]*M for _ in range(N)]

    # 1. 공격자 선택
    ax, ay = choice_attacker()
    arr[ax][ay] += N + M
    atk_time[ax][ay] = time
    time += 1
    atk[ax][ay] = False
    shoot = arr[ax][ay]

    # 2. 공격 대상 선택
    tx, ty = choice_target(ax, ay)

    # 3. 공격
    if not laser_atk(ax, ay, tx, ty, shoot):
        bomb_atk(ax, ay, tx, ty, shoot)

    # 4. 포탑 부서짐 처리
    break_check()

    # 5. 포탑 정비
    turret_check()

# 6. 최종 출력
print(max_check())
