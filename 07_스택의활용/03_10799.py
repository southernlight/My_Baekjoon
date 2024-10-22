import sys
from collections import deque

parenthesis = sys.stdin.readline().strip()
dq = deque()

l = len(parenthesis)

ans = 0
for i in range(l):
    if parenthesis[i] == "(":
        dq.append(parenthesis[i])
    elif parenthesis[i - 1] == "(":
        dq.pop()
        ans += len(dq)
    else:
        dq.pop()
        ans += 1

print(ans)
