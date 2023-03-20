def solution(record):
    answer = []
    nicknames = {}

    for rec in record:
        sp = rec.split(' ')

        if sp[0] == 'Enter':
            nicknames[sp[1]] = sp[2]
            answer.append([sp[1], '님이 들어왔습니다.'])
        if sp[0] == 'Leave':
            answer.append([sp[1], '님이 나갔습니다.'])
        if sp[0] == 'Change':
            nicknames[sp[1]] = sp[2]

    for a in range(len(answer)):
        answer[a] = nicknames[answer[a][0]] + answer[a][1]

    return answer