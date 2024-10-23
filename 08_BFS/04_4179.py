import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())

maze = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

dq_f = deque()
dist_f = [[sys.maxsize for _ in range(c)] for _ in range(r)]
dq_j = deque()
dist_j = [[sys.maxsize for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        if maze[i][j] == "F":
            dq_f.append([i, j])
            dist_f[i][j] = 1
        elif maze[i][j] == "J":
            dq_j.append([i, j])
            dist_j[i][j] = 1

# 불 BFS
while dq_f:
    cur_x, cur_y = dq_f.popleft()
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if maze[nx][ny] == "#" or dist_f[nx][ny] != sys.maxsize:
            continue
        dist_f[nx][ny] = dist_f[cur_x][cur_y] + 1
        dq_f.append([nx, ny])

# 지훈 BFS
while dq_j:
    cur_x, cur_y = dq_j.popleft()
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if maze[nx][ny] == "#" or dist_j[nx][ny] != sys.maxsize:
            continue
        if dist_j[cur_x][cur_y] + 1 >= dist_f[nx][ny]:
            continue
        dist_j[nx][ny] = dist_j[cur_x][cur_y] + 1
        dq_j.append([nx, ny])

result = sys.maxsize
for x in range(r):
    for y in range(c):
        if x == 0 or x == r - 1 or y == 0 or y == c - 1:
            if dist_j[x][y] != 0:
                result = min(result, dist_j[x][y])

if result == sys.maxsize:
    print("IMPOSSIBLE")
else:
    print(result)
