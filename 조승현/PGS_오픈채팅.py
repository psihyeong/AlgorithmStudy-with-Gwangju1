def solution(record):
    answer = []
    nick = {}
    for r in record:
        arr = r.split()
        log = arr[0]
        if log == 'Enter' or log == 'Change':
            nick[arr[1]] = arr[2]
    for r in record:
        arr = r.split()
        log = arr[0]
        if log == 'Enter':
            answer.append(f'{nick[arr[1]]}님이 들어왔습니다.')
        elif log == 'Leave':
            answer.append(f'{nick[arr[1]]}님이 나갔습니다.')
    
    return answer