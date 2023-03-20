N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key = lambda x: x[1])
max_idx, maxV = arr[-1][0], arr[-1][1]
arr.sort()
sumV = 0
val, val_idx= arr[0][1], arr[0][0]

for i in range(N):
    if arr[i][0] == max_idx:
        sumV += maxV + (max_idx - val_idx) * val
        break
    if val < arr[i][1]:
        sumV += (arr[i][0] - val_idx) * val
        val = arr[i][1]
        val_idx = arr[i][0]

val, val_idx = arr[-1][1], arr[-1][0]

for i in range(N-1, -1, -1):
    if arr[i][0] == max_idx:
        sumV += (val_idx - max_idx) * val
        break
    if val < arr[i][1]:
        sumV += (val_idx - arr[i][0]) * val
        val = arr[i][1]
        val_idx = arr[i][0]
print(sumV)
