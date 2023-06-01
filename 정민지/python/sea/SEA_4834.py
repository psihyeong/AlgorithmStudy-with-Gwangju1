import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    cards = input()
    card_count = [0] * 10
    sort_list = [0] * 10

    for card in cards:
        card_count[int(card)] += 1

    max_val = - sys.maxsize -1
    max_idx = 0
    for idx in range(10):
        if card_count[idx] >= max_val:
            max_idx = idx

    print("#{} {} {}".format(tc, max_idx, max_val))
