# 1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.

# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )

def solution(n, k, start, lst):
    global cnt

    if len(lst) == n:
        if sum(lst) == k:
            cnt += 1
        return

    for i in range(start, 13):
        lst.append(i)
        solution(n, k, i + 1, lst)
        lst.pop()


for tc in range(int(input())):
    n, k = map(int, input().split())
    cnt = 0
    solution(n, k, 1, [])
    print(f'#{tc + 1} {cnt}')
