from collections import defaultdict
class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        output = 1000000
        cache = defaultdict(list)
        for i, num in enumerate(nums):
            cache[num].append(i)
        
        for _num, indices in cache.items():
            for i in range(len(indices) - 2):
                output = min(output, 2*(indices[i+2] - indices[i]))

        return output if output != 1000000 else -1