# import sys
# input = sys.stdin.readline

for tc in range(int(input())):
    dic = {}

    n = int(input())
    lst = list(map(int, input()))

    for i in range(n):
        if lst[i] in dic.keys():
            dic[lst[i]] += 1
        else:
            dic[lst[i]] = 1

    mx, idx = 0, 0
    for k, v in dic.items():
        if v > mx:
            mx, idx = v, k
        elif v == mx:
            if idx < k:
                idx = k

    print(dic)
