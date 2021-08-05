def increment_string(s):
    if s and s[-1].isdigit():
        return increment_string(s[:-1]) + "0" if s[-1] == "9" else s[:-1] + `int(s[-1]) + 1`
    return s + "1"

#def increment_string(strng):
#    
#    #strip the decimals from the right
#    stripped = strng.rstrip('1234567890')
#    
#    # get the part of strng that was stripped
#    ints = strng[len(stripped):]
#    
#    if len(ints) == 0:
#        return strng + '1'
#    else:
#        # find the length of ints
#        length = len(ints)
#    
#        # add 1 to ints
#        new_ints = 1 + int(ints)
#    
#        # pad new_ints with zeroes on the left
#        new_ints = str(new_ints).zfill(length)
#    
#        return stripped + new_ints