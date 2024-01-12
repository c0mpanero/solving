# TODO: i couldn't do it with my knowledge
# kata: https://www.codewars.com/kata/54d496788776e49e6b00052f/train/python

def primes():
    current = 1
    while True:
        current += 1
        while True:
            for i in range(2, current // 2 + 1):
                if current % i == 0:
                    current += 1
                    break
            else:
                break
        yield current

def isthere(n, lst):
    for e in lst:
        if e % n == 0:
            return True
    return False

def sum_for_list(lst):
    res = []
    for p in primes():
        if not isthere(p, lst):
            break
        else:
            res.append([p, sum([e for e in lst if e % p == 0])])
    return res
