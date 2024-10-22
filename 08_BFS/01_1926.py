import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
vis = [[False] * m for _ in range(n)]


def bfs(i, j):
    dq = deque()
    dq.append([i, j])
    vis[i][j] = True

    width = 1

    while dq:
        cur_x, cur_y = dq.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if paper[nx][ny] == 0 or vis[nx][ny] == True:
                continue
            vis[nx][ny] = True
            dq.append([nx, ny])
            width += 1
    return width


cnt = 0
printing = 0
for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and vis[i][j] == False:
            printing = max(bfs(i, j), printing)
            cnt += 1


print(cnt)
print(printing)
