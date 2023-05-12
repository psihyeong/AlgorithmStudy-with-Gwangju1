for tc in range(int(input())):
    lst = [[0 for _ in range(10)] for _ in range(10)]

    for n in range(int(input())):
        sr, sc, er, ec, color = map(int, input().split())

        for i in range(sr, er + 1):
            for j in range(sc, ec + 1):
                if lst[i][j] == 0:
                    lst[i][j] = color
                elif lst[i][j] == 3 - color:
                    lst[i][j] = 3

    cnt = 0
    for i in range(10):
        for j in range(10):
            if lst[i][j] == 3:
                cnt += 1

    print(f'#{tc + 1} {cnt}')
