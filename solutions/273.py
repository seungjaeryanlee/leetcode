"""
Solution for Algorithms #273: Integer to English Words

- N: Number of digits
- Time Complexity: O(N)
- Space Complexity : O(N)

Runtime: 36 ms, faster than 90.30% of Python3 online submissions for Integer to English Words.
Memory Usage: 13.1 MB, less than 90.82% of Python3 online submissions for Integer to English Words.
"""
int_to_str = {
    0: '',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
}
int_to_str_tens = {
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen',
    14: 'Fourteen',
    15: 'Fifteen',
    16: 'Sixteen',
    17: 'Seventeen',
    18: 'Eighteen',
    19: 'Nineteen',
}
int_to_str_second = {
    2: 'Twenty',
    3: 'Thirty',
    4: 'Forty',
    5: 'Fifty',
    6: 'Sixty',
    7: 'Seventy',
    8: 'Eighty',
    9: 'Ninety',
}
t_m_b_t = ['', 'Thousand', 'Million', 'Billion', 'Trillion']


class Solution:
    def _three_digit_ntw(self, num):
        output = ''
        if num >= 100:
            output += int_to_str[num // 100] + ' Hundred '
            num -= num // 100 * 100
        if num >= 20:
            output += int_to_str_second[num // 10] + ' '
            num -= num // 10 * 10
        if num >= 10:
            output += int_to_str_tens[num] + ' '
            num = 0
        if num != 0:
            output += int_to_str[num]

        return output.strip()

    def numberToWords(self, num: int) -> str:
        if not num: return "Zero"

        output = ''
        t_m_b_t_count = 0
        while num:
            num, last_three_digits = num // 1000, num % 1000
            if last_three_digits != 0:
                output = self._three_digit_ntw(last_three_digits) + ' ' + t_m_b_t[t_m_b_t_count] + ' ' + output
            t_m_b_t_count += 1

        return output.strip()
