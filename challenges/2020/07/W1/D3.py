"""
Solution for July LeetCoding Challenges Week 1 Day 3: Prison Cells After N Days
"""
class Solution:
    """
    Find a pattern (loop), and use it to our advantage.

    Uses the fact that there are only 64 possible cell configurations, so the pattern is at most 64 days long.

    - Number of days: N
    - Space Complexity: O(1)
    - Time Complexity: O(1)

    If we consider the number of cells as a variable (K), the complexity equation changes.

    - Space Complexity: O(K min(N, 2^K))
    - Time Complexity: O(K min(N, 2^K))

    Runtime: 48 ms / 30.20%
    Memory Usage: 13.8 MB / 69.62%
    """
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def forward(cells):
            # First and last elements are always 0 after day 0
            updated_cells = [0] * len(cells)
            for i in range(1, len(cells) - 1):
                updated_cells[i] = int(cells[i - 1] == cells[i + 1])

            return updated_cells

        # Run forward until a pattern is found
        pattern_found = False
        pattern = []
        for day_idx in range(N):
            if cells not in pattern:
                pattern.append(cells)
                cells = forward(cells)
            else:
                pattern_found = True
                break

        # All days past before pattern found: return
        if not pattern_found:
            return cells

        # Cutoff history before pattern
        pattern = pattern[pattern.index(cells):]

        # Use pattern
        return pattern[(N - day_idx) % len(pattern)]
