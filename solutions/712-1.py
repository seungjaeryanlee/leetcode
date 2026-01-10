from functools import lru_cache
class Solution:
    
    @lru_cache(maxsize=2000)
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # Thought 1:
        # Find all maximal intersections
        # Compute delete sum for each maximal intersection
        # Get minimum

        # Thought 2:
        # Computing delete sum is trivial as we can do ASCII(s1) + ASCII(s2) - 2 x ASCII(max_intersection)

        # Thought 3:
        # Is maximal intersection unique?
        # S1 = "ac", S2 = "ca": both "a" and "c" is "maximal"
        # Similarly, S1 = "acb", S2 = "cab" -> both "ab" and "cb" is maximal

        # Thought 4:
        # So maybe we could just recursively call minimumDeleteSum then?

        # Edge cases: at least one string is empty
        if not s1 and not s2:
            return 0
        elif not s1:
            return sum(ord(c) for c in s2)
        elif not s2:
            return sum(ord(c) for c in s1)
        
        if s1[0] == s2[0]:
            # May be better to pass indices instead of creating new list
            return self.minimumDeleteSum(s1[1:], s2[1:])
        else:
            return min(
                self.minimumDeleteSum(s1, s2[1:]) + ord(s2[0]),
                self.minimumDeleteSum(s1[1:], s2) + ord(s1[0])
            )

# Editorial points out great other solutions (1. Iterative, 2. Space-efficient iterative)