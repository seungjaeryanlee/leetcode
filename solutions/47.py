from collections import Counter


class Solution1:
    def recursion(self, num_counts: dict[int, int]) -> list[list[int]]:
        if sum(num_counts.values()) == 0:
            return [[]]

        output = []
        for num, count in num_counts.items():
            if count > 0:
                new_num_counts = num_counts.copy()
                new_num_counts[num] -= 1
                for sublist in self.recursion(new_num_counts):
                    output.append([num] + sublist)

        return output

    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        num_counts = Counter(nums)

        return self.recursion(num_counts)


        from collections import Counter


class Solution2:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        output = []

        num_counts = Counter(nums)
        candidate = []
        
        def backtrack():
            if len(candidate) == len(nums):
                output.append(candidate.copy())
                return

            for num, count in num_counts.items():
                if count > 0:
                    candidate.append(num)
                    num_counts[num] -= 1

                    backtrack()

                    num = candidate.pop()
                    num_counts[num] += 1

        backtrack()
        return output
