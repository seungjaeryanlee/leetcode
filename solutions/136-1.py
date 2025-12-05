class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cache = set()
        for num in nums:
            if num in cache:
                cache -= {num}
            else:
                cache.add(num)
        
        return list(cache)[0]
