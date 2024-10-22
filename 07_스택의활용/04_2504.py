import sys
from collections import deque

equation = sys.stdin.readline().strip()
n = len(equation)

dq = deque()
mul = 1
result = 0
is_right = True
for i in range(n):

    if i == 0 and (equation[i] == ")" or equation[i] == "]"):
        is_right = False
        break

    if equation[i] == "(":
        mul *= 2
        dq.append("(")
    elif equation[i] == "[":
        mul *= 3
        dq.append("[")
    elif equation[i] == ")":
        if len(dq) == 0 or dq[-1] != "(":
            is_right = False
            break
        dq.pop()
        if equation[i - 1] == "(":
            result += mul
            mul //= 2
        else:
            mul //= 2
    else:
        if len(dq) == 0 or dq[-1] != "[":
            is_right = False
            break
        dq.pop()
        if equation[i - 1] == "[":
            result += mul
            mul //= 3
        else:
            mul //= 3

if len(dq) != 0:
    is_right = False

if is_right == True:
    print(result)
else:
    print(0)
