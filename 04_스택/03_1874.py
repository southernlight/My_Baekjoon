from collections import deque

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

dq = deque()
ans = []
cur = 0
flag = True
for i in range(n):
    while True:
        if len(dq) == 0:
            cur += 1
            dq.append(cur)
            ans.append("+")
        else:
            if dq[-1] < arr[i]:
                cur += 1
                dq.append(cur)
                ans.append("+")
            elif dq[-1] > arr[i]:
                ans.append("NO")
                flag = False
                break
            else:
                dq.pop()
                ans.append("-")
                break

if flag == False:
    print("NO")
else:
    for pm in ans:
        print(pm)
