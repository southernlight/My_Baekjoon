import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

tomatoes = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dist = [[-1 for _ in range(m)] for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def is_initially_all_ripped():
    for i in range(n):
        for j in range(m):
            if tomatoes[i][j] == 0:
                return False
    return True


mx = -1


def is_all_ripped():
    global mx
    for i in range(n):
        for j in range(m):
            if tomatoes[i][j] == 0 and dist[i][j] == -1:
                return False
            mx = max(mx, dist[i][j])
    return True


dq = deque()
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            dq.append([i, j])
            dist[i][j] = 0

while dq:
    cur_x, cur_y = dq.popleft()

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if tomatoes[nx][ny] == -1 or dist[nx][ny] != -1:
            continue
        dq.append([nx, ny])
        dist[nx][ny] = dist[cur_x][cur_y] + 1

if is_initially_all_ripped() == True:
    print(0)
elif is_all_ripped() == True:
    print(mx)
else:
    print(-1)
