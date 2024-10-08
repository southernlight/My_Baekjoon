import sys

n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
v = int(input())

ans = 0
for num in numbers:
    if num == v:
        ans += 1

print(ans)
