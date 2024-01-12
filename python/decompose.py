# TODO: couldn't do it with my knowledge
# kata: https://www.codewars.com/kata/54eb33e5bc1a25440d000891/train/python

def strict_inc(lst):
    c = lst[0]
    for v in sorted(lst[1:]):
        if v <= c: return False
        c = v
    return True

def decompose(n):
    ...
