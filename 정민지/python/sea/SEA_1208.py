# import sys
# input = sys.stdin.readline

for tc in range(1, 11):

    n = int(input())
    lst = list(map(int, input().split()))

    for i in range(n):
        lst[lst.index(max(lst))] -= 1
        lst[lst.index(min(lst))] += 1

    print(f'#{tc} {max(lst) - min(lst)}')
