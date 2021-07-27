def make_readable(seconds):
    min, seconds = divmod(seconds, 60)
    hours, min = divmod(min, 60)
    return f'{hours:02d}:{min:02d}:{seconds:02d}'

print(make_readable(int(input())))

#return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60) # one line