
n, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

# 성별 0 -> 여학생 1 -> 남학생, 학년
# 조건 : 성별이 같은 사람끼리, 같은 학년 학생끼리

# arr1 은 여자방, arr2 는 남자방
female_room = [0 for _ in range(6)]
male_room = [0 for _ in range(6)]

for l in lst:
    if l[0] == 0:
        female_room[l[1]-1] += 1
    else:
        male_room[l[1]-1] += 1

for i in range(6):
    male_room[i] = male_room[i] // k if male_room[i] % k == 0 else male_room[i] // k + 1
    female_room[i] = female_room[i] // k if female_room[i] % k == 0 else female_room[i] // k + 1

print(sum(male_room + female_room))