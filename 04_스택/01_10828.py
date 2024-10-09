from collections import deque
import sys

dq = deque()

n = int(input())
for i in range(n):
    command = list(sys.stdin.readline().split())
    if command[0] == "push":
        dq.append(command[1])
    elif command[0] == "pop":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif command[0] == "size":
        print(len(dq))
    elif command[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
