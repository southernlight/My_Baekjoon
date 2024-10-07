import sys

mul = 1
count = [0 for _ in range(10)]

for i in range(3):
    mul *= int(input())

for c in str(mul):
    count[int(c)] += 1

for c in count:
    print(c)
