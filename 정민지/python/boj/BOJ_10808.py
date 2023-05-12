import sys
input = sys.stdin.readline

quest = list(input().strip())
result = [0 for _ in range(26)]

for q in quest:
    result[ord(q)-97] += 1

print(' '.join(map(str, result)))