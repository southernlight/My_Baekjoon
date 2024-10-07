import sys

S = input()
counts = [0 for _ in range(ord("z") - ord("a") + 1)]

for c in S:
    counts[ord(c) - ord("a")] += 1

for n in counts:
    print(n, end=" ")
