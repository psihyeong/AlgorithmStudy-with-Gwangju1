import sys
input = sys.stdin.readline

for tc in range(1):
    n = int(input())
    lst = list(map(int, input().split()))

    result = 0
    for i in range(2, len(lst)-2):
        val = lst[i] - max(lst[i-2], lst[i-1], lst[i+1], lst[i+2])
        if val > 0:
            result += val

    print(f'#{tc+1} {result}')