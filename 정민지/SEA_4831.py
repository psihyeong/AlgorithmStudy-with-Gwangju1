for tc in range(int(input())):
    k, n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    station = [0 for _ in range(n + 1)]

    for l in lst:
        station[l] = 1

    idx = 0
    result = 0
    while idx + k < n:
        # 출발지에서 k 를 더한 (=가장 큰 도착지)가 종점보다 크거나 같은지 확인
        # 종점까지 도착 못했을 때
        # 갈 수 있는 정류장 중 충전기가 있는 가장 큰 인덱스를 찾는다.
        for i in range(idx + k, idx, -1):
            if station[i] == 1:
                idx = i
                result += 1
                break
        else:
            result = 0
            break

    print(f'#{tc+1} {result}')