def move_zeros(lst):
    return [n for n in lst if n != 0] + [0 for _ in range(lst.count(0))]
