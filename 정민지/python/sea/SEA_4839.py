for tc in range(int(input())):
    all_page, a_find, b_find = map(int, input().split())
    a_left, b_left = 1, 1
    a_right, b_right = all_page, all_page
    a_center, b_center = (1 + all_page) // 2, (1 + all_page) // 2
    result = ""

    while True:

        if a_center == a_find and b_center == b_find:
            result = "0"
            break

        if a_center == a_find:
            result = "A"
            break

        if b_center == b_find:
            result = "B"
            break

        if a_center < a_find:
            a_left = a_center

        if a_center > a_find:
            a_right = a_center

        if b_center < b_find:
            b_left = b_center

        if b_center > b_find:
            b_right = b_center

        a_center, b_center = (a_left + a_right) // 2, (b_left + b_right) // 2

    print(f'#{tc+1} {result}')