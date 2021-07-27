from math import sqrt
def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i <= sqrt(num):    
        if num%i == 0:
            return False
        i += 1
    return True 

#from math import sqrt
#def is_prime(n):
#  return n > 1 and all(n % d for d in xrange(2, int(sqrt(n)) + 1))

#import gmpy2
#def is_prime(num):
#  return gmpy2.is_prime(num) if num > 0 else False