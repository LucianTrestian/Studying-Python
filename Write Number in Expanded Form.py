def expanded_form(num):
    result = []

    for index, digit in enumerate(str(num)[::-1]):
        if int(digit) != 0:
            result.append(digit + ('0' * index))

    return ' + '.join(result[::-1])


#def expanded_form(num):
#    num = list(str(num))
#    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')