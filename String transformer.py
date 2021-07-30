def string_transformer(s):
    s = [i for i in s.swapcase().split(' ')]
    s.reverse()
    return ' '.join(s)

#def string_transfirmer(s):
#   return ' '.join(s.swapcase().split(' ')[::-1])