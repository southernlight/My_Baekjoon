import sys

n = int(input())
a = ord("a")
z = ord("z")

for i in range(n):
    flag = True
    occur = [0 for _ in range(z - a + 1)]

    first, second = sys.stdin.readline().split()
    if len(first) != len(second):
        flag = False
    else:
        for c in first:
            occur[ord(c) - a] += 1
        for c in second:
            occur[ord(c) - a] -= 1
        if all(x == 0 for x in occur):
            flag = True
        else:
            flag = False
    if flag == True:
        print("Possible")
    else:
        print("Impossible")
