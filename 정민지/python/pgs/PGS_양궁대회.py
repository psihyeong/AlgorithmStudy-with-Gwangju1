def dfs(n, N, ryans, apeachs):
    global maxVal
    global maxScore

    if N == n:
        ryanScore, apeachScore = 0, 0

        for i in range(11):
            if ryans[i] != 0 or apeachs[i] != 0:
                if ryans[i] > apeachs[i]:
                    ryanScore += (10-i)
                if apeachs[i] > ryans[i] or ryans[i] == apeachs[i]:
                    apeachScore += (10-i)

        scoreDif = ryanScore - apeachScore
        if maxVal < scoreDif:
            maxVal = scoreDif
            maxScore = ryans[:]
        return
    else:
        for i in range(11):
            ryans[i] += 1
            dfs(n, N+1, ryans, apeachs)
            ryans[i] -= 1

def solution(n, info):
    global maxVal
    global maxScore
    answer = []

    dfs(n, 0, [0 for i in range(11)], info)

    if maxVal == -1:
        maxScore = [-1]
    return maxScore

maxVal = -1
maxScore = []

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
# print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
# print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))