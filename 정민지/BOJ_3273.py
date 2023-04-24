import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
x = int(input())

# lst에서 lst[i] + lst[j] == x 를 만족하는 쌍의 숫자?
# 포인터 문제

lst.sort()
startIdx, endIdx = 0, n-1
result = 0
while startIdx < endIdx:
    if lst[startIdx] + lst[endIdx] > x:
        endIdx -= 1
        continue

    if lst[startIdx] + lst[endIdx] == x:
        result += 1
        startIdx += 1
        endIdx -= 1
        continue

    if lst[startIdx] + lst[endIdx] < x:
        startIdx += 1
        continue


print(result)