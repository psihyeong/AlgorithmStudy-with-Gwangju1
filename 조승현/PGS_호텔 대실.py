def solution(book_time):
    answer = 0
    cnt = {}
    
    for time in book_time:
        a = time[0].split(':')
        start = int(a[0]) * 60 + int(a[1])
        
        b = time[1].split(':')
        end = int(b[0]) * 60 + int(b[1]) + 10
        
        for i in range(start, end):
            if not cnt.get(i):
                cnt[i] = 1
            else:
                cnt[i] += 1

    answer = max(cnt.values())
    
    return answer