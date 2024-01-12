# kata: https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python

table = {
    "I"	 = 1,
    "IV" = 4,
    "V"	 = 5,
    "X"	 = 10,
    "L"	 = 50,
    "C"	 = 100,
    "D"	 = 500,
    "M"	 = 1000,
}

def take_parts(n: int) -> list:
    return [
        int(str(n)[i]) * (10 ** (3-i)) for i in range(4)
    ]

class RomanNumerals:
    @staticmethod
    def to_roman(val: int) -> str:
        parts = take_parts(val)

    @staticmethod
    def from_roman(val: str) -> int:
        parts = take_parts(val)

