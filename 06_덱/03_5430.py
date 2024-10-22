import sys
from collections import deque
import re


def solve():

    change = [1, 0]

    t = int(input())

    for _ in range(t):
        is_error = False
        is_reverse = 0
        dq = deque()
        command = sys.stdin.readline().strip()
        n = int(input())
        numbers = sys.stdin.readline().strip()
        numbers = re.findall(r"\d+", numbers)
        numbers = [int(num) for num in numbers]

        for num in numbers:
            dq.append(num)
        for c in command:
            if c == "R":
                is_reverse = change[is_reverse]
            else:
                if is_reverse == 0:  # 정방향
                    if len(dq) == 0:
                        print("error")
                        is_error = True
                        break
                    else:
                        dq.popleft()

                else:
                    if len(dq) == 0:
                        print("error")
                        is_error = True
                        break
                    else:
                        dq.pop()  # 역방향
        if is_error == True:
            continue

        if is_reverse == 0:
            print("[", end="")
            for i in range(len(dq)):
                if i == len(dq) - 1:
                    print(dq[i], end="")
                else:
                    print(dq[i], end=",")
            print("]")
        else:
            print("[", end="")
            for i in range(len(dq) - 1, -1, -1):
                if i == 0:
                    print(dq[i], end="")
                else:
                    print(dq[i], end=",")
            print("]")


solve()
