import sys
from collections import deque

t = int(input())
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
m = 0
n = 0
k = 0


def bfs(x, y, cabages, vis):
    global n, m
    dq = deque()
    dq.append([x, y])
    vis[x][y] = True

    while dq:
        cur_x, cur_y = dq.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if cabages[nx][ny] == 0 or vis[nx][ny] == True:
                continue
            vis[nx][ny] = True
            dq.append([nx, ny])
    return 1


for _ in range(t):
    res = 0
    m, n, k = map(int, sys.stdin.readline().split())
    cabages = [[0 for _ in range(m)] for _ in range(n)]
    vis = [[False for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        y, x = map(int, sys.stdin.readline().split())
        cabages[x][y] = 1

    for x in range(n):
        for y in range(m):
            if cabages[x][y] == 1 and vis[x][y] == False:
                res += bfs(x, y, cabages, vis)
    print(res)
