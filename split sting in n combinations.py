def solution(s):
    list=[]
    for i in range(0,len(s),2):
        list.append(s[i:i+2])
    if len(list) != 0:
        if len(list[-1]) != 2:
            list[-1] += '_'
    return list  

solution(input())


#def solution(s):
#   return [s[x:x+2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]

#import re
#def solution(s):
#    return re.findall(".{2}", s + "_")