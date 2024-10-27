import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

dist = [-1 for _ in range(100001)]
dq = deque()

dq.append(n)
dist[n] = 0

while dq:
    cur = dq.popleft()

    for i in range(3):
        if i == 0:
            nxt = cur - 1
        elif i == 1:
            nxt = cur + 1
        else:
            nxt = 2 * cur

        if nxt < 0 or nxt > 100000:
            continue
        if dist[nxt] != -1:
            continue
        dist[nxt] = dist[cur] + 1
        dq.append(nxt)

print(dist[k])
