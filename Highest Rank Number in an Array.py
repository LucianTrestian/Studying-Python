from collections import Counter

def highest_rank(arr):
    if arr:
        c = Counter(arr)
        m = max(c.values())
        return max(k for k,v in c.items() if v==m)

#def highest_rank(arr):
#    return sorted(arr,key=lambda x: (arr.count(x),x))[-1]