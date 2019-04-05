class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_in_substr = []
        max_substr_len = 0
        for c in s:
            if c in c_in_substr:
                # Update max
                max_substr_len = max_substr_len if max_substr_len > len(c_in_substr) else len(c_in_substr)
                # print('{}: {}'.format(c_in_substr, max_substr_len))
                # Delete until substring no longer contains same letters
                while c in c_in_substr:
                    del c_in_substr[0]
            c_in_substr.append(c)
        
        max_substr_len = max_substr_len if max_substr_len > len(c_in_substr) else len(c_in_substr)
        # print('{}: {}'.format(c_in_substr, max_substr_len))

        return max_substr_len
