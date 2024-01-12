def calculate(t, b):
    a = t[1]

    match t[0]:
        case 'times':
            return b * a
        case 'divided_by':
            return b // a
        case 'plus':
            return b + a
        case 'minus':
            return b - a
    
def zero(t=None):
    if t is None:
        return 0
    return calculate(t, 0)

def one(t=None):
    if t is None:
        return 1
    return calculate(t, 1)

def two(t=None):
    if t is None:
        return 2
    return calculate(t, 2)

def three(t=None):
    if t is None:
        return 3
    return calculate(t, 3)

def four(t=None):
    if t is None:
        return 4
    return calculate(t, 4)

def five(t=None):
    if t is None:
        return 5
    return calculate(t, 5)

def six(t=None):
    if t is None:
        return 6
    return calculate(t, 6)

def seven(t=None):
    if t is None:
        return 7
    return calculate(t, 7)

def eight(t=None):
    if t is None:
        return 8
    return calculate(t, 8)

def nine(t=None):
    if t is None:
        return 9
    return calculate(t, 9)

def plus(n):
    return ('plus', n)

def minus(n):
    return ('minus', n)

def times(n):
    return ('times', n)

def divided_by(n):
    return ('divided_by', n)
