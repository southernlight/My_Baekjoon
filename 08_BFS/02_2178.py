import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

maze = []
dist = [[0 for _ in range(m)] for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(n):
    s = input()
    tmp = []
    for i in range(m):
        tmp.append(int(s[i]))
    maze.append(tmp)

dq = deque()
dq.append([0, 0])
dist[0][0] = 1

while dq:
    cur_x, cur_y = dq.popleft()

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if maze[nx][ny] == 0 or dist[nx][ny] != 0:
            continue
        dist[nx][ny] = dist[cur_x][cur_y] + 1
        dq.append([nx, ny])

print(dist[n - 1][m - 1])
