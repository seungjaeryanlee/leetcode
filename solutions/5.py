class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Handle empty string input
        if not s:
            return ''

        found_palindrome = s[0]
        found_len = 1

        # Check odd number palindrome
        for mid_i, mid_c in enumerate(s):
            # Maximum length of palindrome with middle index mid_i
            max_half_len = min(mid_i, (len(s) - 1) - mid_i)

            # Skip if palindrome of bigger size possible is already found
            if found_len >= 2 * max_half_len + 1:
                continue

            # Find biggest palindrome with center mid_i
            found_half_len = 0
            found_end = False
            for j in range(1, max_half_len+1):
                # End of palindrome
                if s[mid_i - j] != s[mid_i + j]:
                    found_half_len = j-1
                    found_end = True
                    break
            if not found_end:
                found_half_len = max_half_len

            # Update found_palindrome if big enough
            if  2*found_half_len + 1 > found_len:
                found_palindrome = s[mid_i - (found_half_len):mid_i + (found_half_len)+1]
                found_len = 2*found_half_len + 1

        # Check even number palindrome
        for mid_i, mid_c in enumerate(s):
            # Use s[mid_i] and s[mid_i+1] as center chars
            if mid_i+1 > len(s) - 1:
                break
            if s[mid_i] != s[mid_i+1]:
                continue

            # Maximum length of palindrome with middle index mid_i and mid_i+1
            max_half_len = min(mid_i, (len(s)-1) - (mid_i+1))

            # Skip if palindrome of bigger size possible is already found
            if found_len >= 2 * max_half_len + 2:
                continue

            # Find biggest palindrome with center mid_i
            found_half_len = 0
            found_end = False
            for j in range(1, max_half_len+1):
                # End of palindrome
                if s[mid_i - j] != s[(mid_i+1) + j]:
                    found_half_len = j-1
                    found_end = True
                    break
            if not found_end:
                found_half_len = max_half_len

            # Update found_palindrome if big enough
            if  2*found_half_len + 2 > found_len:
                found_palindrome = s[mid_i - (found_half_len):(mid_i+1) + (found_half_len)+1]
                found_len = 2*found_half_len + 2


        return found_palindrome
