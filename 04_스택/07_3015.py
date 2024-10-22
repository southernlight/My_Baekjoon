import sys
from collections import deque

n = int(input())
heights = []
for i in range(n):
    heights.append(int(sys.stdin.readline().strip()))

dq = deque()

result = 0
for h in heights:
    while len(dq) != 0 and dq[-1][0] < h:
        result += dq.pop()[1]

    if len(dq) == 0:
        dq.append((h, 1))
        continue

    if dq[-1][0] == h:
        cnt = dq.pop()[1]
        result += cnt

        if len(dq) != 0:
            result += 1
        dq.append((h, cnt + 1))

    else:
        dq.append((h, 1))
        result += 1

print(result)
