"""
Solution for July LeetCoding Challenges Week 2 Day 7: Angle Between Hands of a Clock
"""
class Solution:
    """
    Compute absolute positions of each hand and get their minimum distance

    - Space Complexity: O(1)
    - Time Complexity: O(1)

    Runtime: 20 ms / 99.58%
    Memory Usage: 13.8 MB / 62.34%
    """
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = 360 / 12 * (hour % 12 + minutes / 60)
        minute_angle = 360 / 60 * minutes
        distance = abs(hour_angle - minute_angle)

        return min(distance, 360 - distance)
