def make_readable(seconds):
    min, seconds = divmod(seconds, 60)
    hours, min = divmod(min, 60)
    return f'{hours:02d}:{min:02d}:{seconds:02d}'

print(make_readable(int(input())))