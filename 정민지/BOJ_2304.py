import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort()
col_arr = [i[1] for i in arr]
maxVal = max(col_arr)
arrMaxIdx = col_arr.index(maxVal)

result = 0
idx, val = arr[0][0], arr[0][1]
for i in range(1, arrMaxIdx+1):
    if val < arr[i][1]:
        result += (arr[i][0] - idx) * val
        idx, val = arr[i][0], arr[i][1]

idx, val = arr[-1][0], arr[-1][1]
for i in range(N-2, arrMaxIdx-1, -1):
    if val < arr[i][1]:
        result += (idx - arr[i][0]) * val
        idx, val = arr[i][0], arr[i][1]

result += (idx - arr[arrMaxIdx][0] + 1) * maxVal

print(result)