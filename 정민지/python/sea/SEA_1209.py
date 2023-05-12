# import sys
# input = sys.stdin.readline

for tc in range(1, 11):
    n = int(input())
    lst = []

    maxVal = 0
    for i in range(100):
        row = list(map(int, input().split()))
        lst.append(row)

        if sum(row) > maxVal:
            maxVal = sum(row)

    sumVal2, sumVal3 = 0, 0
    for j in range(100):

        sumVal = 0
        for k in range(100):
            sumVal += lst[k][j]

        if sumVal > maxVal:
            maxVal = sumVal

        sumVal2 += lst[j][j]
        sumVal3 += lst[j][99-j]

    if sumVal2 > maxVal:
        maxVal = sumVal2

    if sumVal3 > maxVal:
        maxVal = sumVal3






