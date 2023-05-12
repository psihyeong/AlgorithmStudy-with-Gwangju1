# import sys
# input = sys.stdin.readline

# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
#
# 다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100

for tc in range(int(input())):

    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    sort_lst = []

    for idx in range(5):
        sort_lst.append(lst[n-1-idx])
        sort_lst.append(lst[idx])

    print(f'#{tc+1} {" ".join(map(str, sort_lst))}')
