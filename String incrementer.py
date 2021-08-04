import re

def increment_string(strng):
    return re.sub(r'[0-9]+$',
                lambda x: f"{str(int(x.group())+1).zfill(len(x.group()))}", 
                strng)

print(increment_string(input()))