import sys
from collections import deque

n = int(input())
arr = []

arr = list(map(int, sys.stdin.readline().split()))
arr_with_i = []

for i in range(n):
    arr_with_i.append((i + 1, arr[i]))

result = []
dq = deque()
dq.append(arr_with_i[n - 1])
result.append(-1)

for i in range(n - 2, -1, -1):
    while len(dq) != 0:
        if arr_with_i[i][1] >= dq[-1][1]:
            dq.pop()
        else:
            break
    if len(dq) == 0:
        result.append(-1)
    else:
        result.append(dq[-1][1])
    dq.append(arr_with_i[i])


for i in range(n - 1, -1, -1):
    print(result[i], end=" ")
