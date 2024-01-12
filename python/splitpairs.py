from textwrap import wrap

def solution(s):
    if len(s) % 2 == 0:
        return wrap(s, 2)

    w = wrap(s, 2)
    w[len(w) - 1] += "_"
    return w
