from typing import no_type_check, no_type_check_decorator


import re
def dashatize(n):
    try:
        return ''.join(['-'+i+'-' if int(i)%2 else i for i in str(abs(n))]).replace('--','-').strip('-')
    except:
        return 'None'   

print(dashatize(input()))

