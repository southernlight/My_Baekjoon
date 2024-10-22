import sys
from collections import deque


while True:

    s = sys.stdin.readline()
    if s == ".\n":
        break

    is_yes = True
    dq = deque()
    for c in s:
        if c == "(" or c == "[":
            dq.append(c)
        elif c == ")":
            if len(dq) == 0:
                is_yes = False
                break
            elif dq[-1] != "(":
                is_yes = False
                break
            else:
                dq.pop()
        elif c == "]":
            if len(dq) == 0:
                is_yes = False
                break
            elif dq[-1] != "[":
                is_yes = False
                break
            else:
                dq.pop()
    if len(dq) != 0:
        is_yes = False
    if is_yes == True:
        print("yes")
    else:
        print("no")
