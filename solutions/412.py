"""
Solution for Algorithms #412: Fizz Buzz

- Time Complexity: O(N)
- Space Complexity: O(N)

Runtime: 52 ms, faster than 90.93% of Python3 online submissions for Fizz Buzz.
Memory Usage: 14.1 MB, less than 78.99% of Python3 online submissions for Fizz Buzz.
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = [0] * n
        for i in range(1, n+1):
            if i % 15 == 0: output[i-1] = 'FizzBuzz'
            elif i % 3 == 0: output[i-1] = 'Fizz'
            elif i % 5 == 0: output[i-1] = 'Buzz'
            else: output[i-1] = str(i)

        return output
