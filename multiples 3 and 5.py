def solution(number):
    n, m = 3, 5  # multiples
    multiples_n = [n * i for i in range(1, number) if n * i < number]
    multiples_m = [m * i for i in range(1, number) if m * i < number]
    return sum(multiples_n + list(set(multiples_m) - set(multiples_n)))
    #Another solution 
    #def solution(number):
    #return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
