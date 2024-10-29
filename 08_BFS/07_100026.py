import sys
from collections import deque

n = int(input())
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

painting = []
painting_blind = []

for i in range(n):
    line = input()
    painting.append([])
    for j in range(n):
        painting[i].append(line[j])

for i in range(n):
    painting_blind.append([])
    for j in range(n):
        if painting[i][j] == "G":
            painting_blind[i].append("R")
        else:
            painting_blind[i].append(painting[i][j])


def bfs(x, y, color, painting):
    dq = deque()
    dq.append([x, y])
    painting[x][y] = "C"

    while dq:
        cur_x, cur_y = dq.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if painting[nx][ny] != color:
                continue
            painting[nx][ny] = "C"
            dq.append([nx, ny])
    return 1


res1 = 0
for x in range(n):
    for y in range(n):
        if painting[x][y] != "C":
            res1 += bfs(x, y, painting[x][y], painting)

res2 = 0
for x in range(n):
    for y in range(n):
        if painting_blind[x][y] != "C":
            res2 += bfs(x, y, painting_blind[x][y], painting_blind)

print(res1, res2)
