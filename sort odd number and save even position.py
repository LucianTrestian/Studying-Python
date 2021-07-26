def sort_array(source_array):
    splited_array = list(map(int, ''.join([i for i in source_array.split(',')]).split()))   # create clear list with integer elemenets 
    odd_array = sorted([i for i in splited_array if i % 2 != 0])    # extract odd numbers
    for index, item in enumerate(splited_array):    #try to insert in splited_array
        if item in odd_array:
            splited_array[index] = odd_array.pop(0)
    return splited_array

print(sort_array(input()))

#def sort_array(source_array):
#   result = sorted([l for l in source_array if l % 2 == 1])
#    for index, item in enumerate(source_array):
#        if item % 2 == 0:
#            result.insert(index, item)
#    return result

#def sort_array(source_array):
#   odds = iter(sorted(v for v in source_array if v % 2))
#    return [next(odds) if i % 2 else i for i in source_array]