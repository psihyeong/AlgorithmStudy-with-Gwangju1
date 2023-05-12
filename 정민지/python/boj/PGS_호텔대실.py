def solution(book_time):
    times = [0 for _ in range(1450)]

    for book in book_time:
        start = book[0].split(':')
        start_hour = int(start[0])
        start_minute = int(start[1])
        start_time = start_hour * 60 + start_minute

        end = book[1].split(':')
        end_hour = int(end[0])
        end_minute = int(end[1])
        end_time = end_hour * 60 + end_minute

        for time in range(start_time, end_time+10):
            times[time] += 1

    return max(times)