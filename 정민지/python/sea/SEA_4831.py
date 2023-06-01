import sys

input = sys.stdin.readline

for tc in range(int(input())):
    k, n, m = map(int, input().split())
    charge_stops = list(map(int, input().split()))

    bus_stops = [i for i in range(n + 1)]

    for charge in charge_stops:
        bus_stops[charge] = 1

    start, cnt = 0, 0
    while start + k < n:

        for idx in range(start + k, start, -1):
            if bus_stops[idx] == 1:
                start = idx
                cnt += 1
                break
        else:
            cnt = 0
            break

    print(f'#{tc + 1} {cnt}')
