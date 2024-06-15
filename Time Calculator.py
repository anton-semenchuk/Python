#The function should add the duration time to the start time and return the result.
def add_time(start, duration, day=''):
    time = start.split(' ')
    time_nums = time[0].split(':')
    time_str = time[1]
    time_hrs = int(time_nums[0])
    time_mins = int(time_nums[1])
    days = 0

    dur = duration.split(':')
    dur_hrs = int(dur[0])
    dur_mins = int(dur[1])

    time_mins += dur_mins   
    if time_mins > 59:
        time_hrs += 1
        time_mins -= 60
    if len(str(time_mins)) == 1:
        time_mins = f'0{time_mins}'

    time_hrs += dur_hrs
    while time_hrs >= 12:
        if time_str == 'AM':
            time_str = 'PM'
        else:
            time_str = 'AM'
            days += 1
        if time_hrs > 12:
            time_hrs -= 12
        else:
            break

    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday","sunday"]
    final_day = ''
    for i, j in enumerate(days_of_week):
        if day and days_of_week[i] == day.lower(): 
            i += days 
            while i > 6:
                i = i % 7
            final_day = days_of_week[i].capitalize()
            break
        i += 1

    days_later = ''
    if days == 1:
        days_later = '(next day)'
    elif days > 1:
        days_later = f'({days} days later)'
    #output
    new_time = f'{time_hrs}:{time_mins} {time_str}'
    if days and not day:
        new_time += f' {days_later}'
    elif days and day:
        new_time += f', {final_day} {days_later}'
    elif day:
        new_time += f', {final_day}'

    print (new_time)
    return new_time

add_time('8:16 PM', '466:02', 'tuesday')