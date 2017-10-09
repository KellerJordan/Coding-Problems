time = input().strip()
period = time[8:]
hr = int(time[:2])
if period == 'AM':
    if hr < 12:
        print(time[:8])
    else:
        print('{:02d}{}'.format(hr - 12, time[2:8]))
else:
    if hr < 12:
        print('{:02d}{}'.format(hr + 12, time[2:8]))
    else:
        print(time[:8])