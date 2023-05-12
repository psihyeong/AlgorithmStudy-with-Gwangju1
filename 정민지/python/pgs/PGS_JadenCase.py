def solution(s):
    arr = s.split(' ')
    print(arr)
    for i in range(len(arr)):
        if arr[i] != '':
            lst = list(arr[i])
            lst[0] = lst[0].upper()

            for j in range(1, len(lst)):
                lst[j] = lst[j].lower()

            arr[i] = ''.join(lst)

    answer = ' '.join(arr)

    return answer


print(solution("for the last  week"))