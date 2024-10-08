import sys

isFemale = 0
isMale = 1

girls = [0 for _ in range(7)]
boys = [0 for _ in range(7)]
n, k = map(int, sys.stdin.readline().split())

for i in range(n):
    gender, grade = map(int, sys.stdin.readline().split())

    if gender == isFemale:
        girls[grade] += 1
    else:
        boys[grade] += 1


for grade in range(1, 7):
    if girls[grade] != 0:
        if (girls[grade] % k) != 0:
            girls[grade] = girls[grade] // k + 1
        else:
            girls[grade] = girls[grade] // k

for grade in range(1, 7):
    if boys[grade] != 0:
        if (boys[grade] % k) != 0:
            boys[grade] = boys[grade] // k + 1
        else:
            boys[grade] = boys[grade] // k

print(sum(girls) + sum(boys))
