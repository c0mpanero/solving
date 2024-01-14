def fib(n, a, b):
    c = a + b
    b = a
    if c * b > n:
        return [c, b, False]
    if c * b == n: 
        return [c, b, True]
    else:
        return f(n, c, b)

    
def productFib(prod):
    return fib(prod, 0, 1)
