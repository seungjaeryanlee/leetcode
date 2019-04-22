"""
Solution for Algorithms #12: Integer to Roman

Runtime: 56 ms, faster than 99.89% of Python3 online submissions for Integer to Roman.
Memory Usage: 13.4 MB, less than 5.14% of Python3 online submissions for Integer to Roman.
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_str = ''

        # M
        roman_str += 'M' * int(num/1000)
        num -=  1000 * int(num/1000)

        # D
        if num >= 900:
            roman_str += 'CM'
            num -= 900
        if num >= 500:
            roman_str += 'D'
            num -= 500

        # C
        if num >= 400:
            roman_str += 'CD'
            num -= 400
        else:
            roman_str += 'C' * int(num/100)
            num -= 100 * int(num/100)

        # L
        if num >= 90:
            roman_str += 'XC'
            num -= 90
        if num >= 50:
            roman_str += 'L'
            num -= 50

        # X
        if num >= 40:
            roman_str += 'XL'
            num -= 40
        else:
            roman_str += 'X' * int(num/10)
            num -= 10 * int(num/10)

        # V
        if num >= 9:
            roman_str += 'IX'
            num -= 9
        if num >= 5:
            roman_str += 'V'
            num -= 5

        # I
        if num == 4:
            roman_str += 'IV'
        else:
            roman_str += 'I' * num

        return roman_str
