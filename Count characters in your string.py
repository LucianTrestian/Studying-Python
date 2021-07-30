def count(string):
    string_count = list(dict.fromkeys(list(string)))    #converts string in list with double caracters for easy count
    return dict([(string_count[i], string.count(string_count[i])) for i in range(len(string_count))])
    #create a dictionary if characters and counts

#from collections import Counter
#def count(string):
#    return Counter(string)

#def count(string):
#  
#    return {i: string.count(i) for i in string}