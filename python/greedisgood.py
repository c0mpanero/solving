# kata: https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python

def score(dice):
    d = {}
    for i in dice:
        d.update({i: dice.count(i)})

    print(d)
    score = 0
    for k, v in d.items():
        print(k, v)
        if k == 1:
            if v < 3: score += 100*v
            if v == 3: score += 1000
            if v == 4: score += 1100
            if v == 5: score += 1200
        if k == 5:
            if v < 3: score += 50*v
            if v == 3: score += 500
            if v == 4: score += 550
            if v == 5: score += 600
        if k in [2, 3, 4, 6]:
            if v >= 3: score += 100*k
    return score
