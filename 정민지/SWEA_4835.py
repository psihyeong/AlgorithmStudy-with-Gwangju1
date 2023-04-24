import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    mx = 0
    mn = 9999999
    for i in range(n-m+1):
        sm = sum(lst[i:i+m])

        if sm > mx:
            mx = sm
        if sm < mn:
            mn = sm

    print(f'#{tc+1} {mx-mn}')