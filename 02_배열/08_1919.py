first = input()
second = input()

occur1 = [0 for _ in range(ord("z") - ord("a") + 1)]
occur2 = [0 for _ in range(ord("z") - ord("a") + 1)]

for c in first:
    occur1[ord(c) - ord("a")] += 1
for c in second:
    occur2[ord(c) - ord("a")] += 1

cnt = 0
for i in range(ord("z") - ord("a") + 1):
    if occur1[i] != occur2[i]:
        cnt += abs(occur1[i] - occur2[i])

print(cnt)
