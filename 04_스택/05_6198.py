from collections import deque

n = int(input())
buildings = []
dq = deque()
for i in range(n):
    height = int(input())
    buildings.append([i + 1, height, 1])


dq.append(buildings[-1])

for i in range(n - 2, -1, -1):
    while len(dq) != 0:
        if buildings[i][1] > dq[-1][1]:
            buildings[i][2] += dq[-1][2]
            dq.pop()
        else:
            break
    dq.append(buildings[i])

res = 0
for i in range(n):
    res += buildings[i][2]

print(res - n)
