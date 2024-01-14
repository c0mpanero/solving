# kata: https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python
# NOTE: couldn't do it...

def is_opposite(a, b):
    if a == b: return False

    return True if len(a + b) in (8, 10) else False

def dir_reduc(arr):
    a = [arr[i-1] for i in range(1, len(arr)) if not is_opposite(arr[i-1], arr[i])]
    b = [a[i-1] for i in range(1, len(a)) if not is_opposite(a[i-1], a[i])]

    return b
