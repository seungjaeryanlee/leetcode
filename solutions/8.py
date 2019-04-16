class Solution:
    def myAtoi(self, str: str) -> int:
        non_whitespace_found = False
        number_str = ''
        for c in str:
            # Whitespace padding
            if not non_whitespace_found and c == ' ':
                continue
            else:
                if not non_whitespace_found and c in ['-', '+']:
                    number_str += c
                elif c in '0123456789':
                    number_str += c
                else:
                    break

                non_whitespace_found = True

        if number_str in ['', '+', '-']:
            return 0

        number = int(number_str)

        if number > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif number < -1 * 2 ** 31:
            return -1 * 2 ** 31
        else:
            return number
