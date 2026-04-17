from collections import defaultdict


class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        last_indices = defaultdict(lambda: -1)
        # queried_nums = [nums[query] for query in queries]
        output = [-1] * len(nums) * 2
        for i, num in enumerate([*nums, *nums]):
            # if num not in queried_nums:
            #     continue
            if last_indices[num] == -1:
                last_indices[num] = i
                # print(dict(last_indices), output)
                continue
            else:
                distance = i - last_indices[num]
                output[i] = distance
                if output[last_indices[num]] > distance or output[last_indices[num]] == -1:
                    output[last_indices[num]] = distance
                last_indices[num] = i
                # print(dict(last_indices), output)

        return [
            (
                min(output[query], output[query + len(nums)])
                if min(output[query], output[query + len(nums)] < len(nums))
                else -1
            )
             for query in queries
        ]
        
