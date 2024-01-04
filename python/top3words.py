"""
kata: https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python
"""

def isword(w):
    w = ''.join(w.split('\''))
    if len(w) != 0 and w.isalpha():
        return True

    return False

def top_3_words(text):
    d = {}
    current_word = ""
    unwanted = ["\\", ",", ";", ":", ".", "/", "?", "!", "-", "+", "_"]
    
    for c in unwanted:
        text = " ".join(text.split(c))

    text = text.lower()
    for word in text.split():
        if word == current_word:
            continue

        if isword(word):
            current_word = word
            d.update( { word: text.split().count(word) })
    
    s = sorted(d.items(), key=lambda word: word[1], reverse=True)
    return [x[0] for x in s[0:3]]

print(
    top_3_words("  '''  ")
)
