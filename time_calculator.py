def add_time(start, duration, day=None):
    
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    d_count = 0
    x = start.split()
    md = x[1]
    t = x[0].split(':')
    d = duration.split(':')
    hr = int(t[0]) + int(d[0])
    m = int(t[1]) + int(d[1])
    while m > 60:
        m -= 60
        hr += 1
    while hr >= 12:
        hr -= 12
        if md == 'AM':
            md = 'PM'
        elif md == 'PM':
            md = 'AM'
            d_count += 1
    if hr == 0:
        hr = 12
    time = ':'.join([str(hr), str(m).rjust(2, '0')])
    new_time = f'{time} {md}'
    
    if d_count == 1 and day == None:
        new_time = f'{new_time} (next day)'
    if d_count > 1 and day == None:
        new_time = f'{new_time} ({d_count} days later)'
    if day != None and (day.lower() in days):
        x = days.index(day.lower())
        if x == 6:
            x = 0
        i = x + d_count
        
        while (i) > 6:
            i -= 7
        pos = days[i] #use while loop here
        if d_count == 0:
            new_time = f'{new_time}, {pos.capitalize()}'
        elif d_count == 1:
            new_time = f'{new_time}, {pos.capitalize()} (next day)'
        elif d_count > 1:
            new_time = f'{new_time}, {pos.capitalize()} ({d_count} days later)'
    return new_time