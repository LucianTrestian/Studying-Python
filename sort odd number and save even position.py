def sort_array(source_array):
    splited_array = list(map(int, ''.join([i for i in source_array.split(',')]).split()))   # create clear list with integer elemenets 
    odd_array = sorted([i for i in splited_array if i % 2 != 0])
    for i in range(0, len(splited_array)):
        n = 0
        if len(odd_array) != 0 or len(splited_array) != 0:
            sorted_array = [splited_array[i] == "" for i in splited_array if i in odd_array]


    return sorted_array

print(sort_array(input()))