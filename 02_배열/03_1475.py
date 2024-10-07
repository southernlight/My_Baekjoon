n = int(input())

count = [0 for _ in range(10)]

for c in str(n):
    count[int(c)] += 1

if (count[6] + count[9]) % 2 == 0:
    count[9] = (count[6] + count[9]) // 2
    count[6] = 0
else:
    count[9] = (count[6] + count[9]) // 2 + 1
    count[6] = 0
print(max(count))
