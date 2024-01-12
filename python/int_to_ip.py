from textwrap import wrap

def int32_to_ip(n):
    n = bin(n)[2:]
    n = '0'*(32 - len(n)) + n
    parts = wrap(n, 8)

    return '.'.join([str(int(p, 2)) for p in parts])
