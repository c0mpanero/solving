from math import log, floor

def zeros(n):
    if n == 0:
        return 0

    return sum([
        floor((n / (5**k))) for k in range (1, floor(log(n, 5)) +1)
    ])
