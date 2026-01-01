class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = []
        increment_flag = True
        for i in range(len(digits) - 1, -1, -1):
            if not increment_flag:
                output.append(digits[i])
                continue

            if digits[i] < 9:
                increment_flag = False
                output.append(digits[i] + 1)
            if digits[i] == 9:
                output.append(0)
        
        if increment_flag:
            output.append(1)

        return output[::-1]
