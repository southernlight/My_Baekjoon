import sys
from collections import deque

n = int(input())
heights = list(map(int, sys.stdin.readline().split()))
towers = []
dq = deque()

for i in range(1, n + 1):
    towers.append((i, heights[i - 1]))

dq.append(towers[0])
print(0, end=" ")

for i in range(1, n):
    while len(dq) != 0:
        if towers[i][1] > dq[-1][1]:
            dq.pop()
        else:
            break

    if len(dq) == 0:
        print(0, end=" ")
    else:
        print(dq[-1][0], end=" ")
    dq.append(towers[i])
