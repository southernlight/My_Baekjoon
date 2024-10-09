from collections import deque

K = int(input())

dq = deque()

for i in range(K):
    n = int(input())
    if n != 0:
        dq.append(n)
    else:
        dq.pop()

print(sum(dq))
