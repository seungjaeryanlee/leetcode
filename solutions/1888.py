class Solution1:
    """Inefficient solution that checks all rotations of the string."""
    def onlyType2(self, s: str) -> int:
        next_char = "1"
        count = 0
        for c in s:
            if c != next_char:
                count += 1
            next_char = "0" if next_char == "1" else "1"
    
        count = min(count, len(s) - count)

        print(s, count)
        return count

    def minFlips(self, s: str) -> int:
        min_count = len(s)
        for i in range(len(s)):
            min_count = min(min_count, self.onlyType2(s[i:] + s[:i]))
        
        return min_count


class Solution2:
    """Efficient solution that uses a sliding window to check all rotations in O(n) time."""
    def _get_targets(self, len_s: int) -> tuple[str, str]:
        target1 = "".join(["0" if i % 2 == 0 else "1" for i in range(2 * len_s)])
        target2 = "".join(["1" if i % 2 == 0 else "0" for i in range(2 * len_s)])

        return target1, target2

    def minFlips(self, s: str) -> int:
        len_s = len(s)
        ss = s + s
        target1, target2 = self._get_targets(len_s)

        diff1, diff2 = 0, 0
        min_flips = len_s
        left = 0
        for right in range(2 * len_s):
            # 1. Add the new character entering the window
            if ss[right] != target1[right]:
                diff1 += 1
            if ss[right] != target2[right]:
                diff2 += 1
            
            # 2. If the window is larger than n, remove the leftmost character
            if (right - left + 1) > len_s:
                if ss[left] != target1[left]:
                    diff1 -= 1
                if ss[left] != target2[left]:
                    diff2 -= 1
                left += 1
            
            # 3. Once the window hits size n, track the minimum
            if (right - left + 1) == len_s:
                min_flips = min(min_flips, diff1, diff2)
                
        return min_flips