N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

maxVal, maxIdx = 0, 0
startIdx, endIdx, arrEndIdx = 1001, 0, 0
for i in range(N):
    if maxVal < arr[i][1]:
        maxVal = arr[i][1]
        maxIdx = arr[i][0]

    if endIdx < arr[i][0]:
        endIdx = arr[i][0]
        arrEndIdx = i

    if startIdx > arr[i][0]:
        startIdx = arr[i][0]

resultArr = []
val, idx = 0, startIdx
for j in range(startIdx, maxIdx + 1):
    for k in range(N):
        if arr[k][0] == j and val < arr[k][1]:
            val = arr[k][1]
    resultArr.append(val)

val = arr[arrEndIdx][1]
resultArr2 = []
for j in range(endIdx, maxIdx, -1):
    for k in range(N):
        if arr[k][0] == j and arr[k][1] <= maxVal and arr[k][1] > val:
            val = arr[k][1]
    resultArr2.append(val)

resultArr2.reverse()
print(sum(resultArr+resultArr2))
