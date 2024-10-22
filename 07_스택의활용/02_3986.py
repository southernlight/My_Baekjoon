import sys
from collections import deque

cnt = 0
n = int(input())
for _ in range(n):

    word = sys.stdin.readline().strip()
    dq = deque()
    for c in word:
        if len(dq) == 0:
            dq.append(c)
        else:
            if dq[-1] != c:
                dq.append(c)
            else:
                dq.pop()
    if len(dq) == 0:
        cnt += 1

print(cnt)
