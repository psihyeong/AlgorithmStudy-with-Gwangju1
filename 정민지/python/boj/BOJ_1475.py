lst = list(input())
arr = [0 for _ in range(10)]

for l in lst:
    arr[int(l)] += 1

arr[9] = arr[6] + arr[9]
arr[6] = 0
arr[9] = arr[9] // 2 if arr[9] % 2 == 0 else arr[9] // 2 + 1
print(max(arr))