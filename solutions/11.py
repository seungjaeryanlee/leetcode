"""
Solution for Algorithms #11: Container with Most Water

Runtime: 60 ms, faster than 85.77% of Python3 online submissions for Container With Most Water.
Memory Usage: 14.6 MB, less than 5.18% of Python3 online submissions for Container With Most Water.
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left_i = 0
        right_i = len(height) - 1
        
        while left_i < right_i:
            if height[left_i] < height[right_i]:
                max_area = max(max_area, height[left_i] * (right_i - left_i))
                left_i += 1
            else:
                max_area = max(max_area, height[right_i] * (right_i - left_i))
                right_i -= 1

        return max_area
