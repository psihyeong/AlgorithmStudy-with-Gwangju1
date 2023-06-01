import sys

input = sys.stdin.readline

for tc in range(int(input())):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    minVal = sys.maxsize
    maxVal = -sys.maxsize - 1

    for i in range(n - m + 1):
        sumVal = sum(lst[i:i + m])

        if sumVal > maxVal:
            maxVal = sumVal
        if sumVal < minVal:
            minVal = sumVal

    print(f'#{tc + 1} {maxVal - minVal}')
