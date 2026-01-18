class Solution:
    def helper_two(self, bottom_left1, top_right1, bottom_left2, top_right2) -> int:
        bottom1, left1 = bottom_left1
        top1, right1 = top_right1
        bottom2, left2 = bottom_left2
        top2, right2 = top_right2

        if left1 > left2:
            bottom1, left1, right1, top1, bottom2, left2, right2, top2 = bottom2, left2, right2, top2, bottom1, left1, right1, top1

        intersecting_height = min(top2, top1) - max(bottom1, bottom2)
        intersecting_width = min(right2, right1) - max(left1, left2)

        if intersecting_height <= 0 or intersecting_width <= 0:
            return 0
        return min(intersecting_height, intersecting_width) ** 2

    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_size = 0
        for i in range(n):
            for j in range(n):
                if i >= j:
                    continue
                
                max_size = max(
                    max_size,
                    self.helper_two(bottomLeft[i], topRight[i], bottomLeft[j], topRight[j])
)

        return max_size