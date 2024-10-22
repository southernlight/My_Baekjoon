import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

dq = deque()

for i in range(1, n + 1):
    dq.append(i)
targets = list(map(int, sys.stdin.readline().split()))


def solve():
    cnt = 0
    for i in range(m):
        for j in range(len(dq)):
            if targets[i] == dq[j]:
                if j <= len(dq) // 2:  # 2번 연산
                    while dq[0] != targets[i]:
                        dq.append(dq.popleft())
                        cnt += 1
                else:  # 3번 연산
                    while dq[0] != targets[i]:
                        dq.appendleft(dq.pop())
                        cnt += 1
                dq.popleft()
                break
    return cnt


print(solve())
