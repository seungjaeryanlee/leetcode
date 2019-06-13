"""
Solution for Algorithms #973: K Closest Points to Origin

Sort points in-place by distance then return subarray.

Runtime: 376 ms, faster than 66.82% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 17 MB, less than 78.34% of Python3 online submissions for K Closest Points to Origin.
"""
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # NOTE Only if modifing points is allowed: else use sorted(points)
        points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
        return points[:K]
