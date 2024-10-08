import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
x = int(input())
nums_TF = [False for _ in range(2000002)]

for num in nums:
    nums_TF[num] = True

ans = 0
for i in range(1, x // 2 + 1):
    if i == x - i:
        continue
    else:
        if nums_TF[i] == True and nums_TF[x - i] == True:
            ans += 1

print(ans)
