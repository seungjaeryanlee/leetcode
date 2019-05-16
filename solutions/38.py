"""
Solution for Algorithms #38: Count and Say

Runtime: 40 ms, faster than 86.78% of Python3 online submissions for Count and Say.
Memory Usage: 13.2 MB, less than 42.67% of Python3 online submissions for Count and Say.
"""
class Solution:
    def count_and_say_seq(self, seq):
        new_seq = ''
        count = 0
        for i in range(len(seq)-1):
            if seq[i] == seq[i+1]:
                count += 1
            else:
                new_seq += '{}{}'.format(count + 1, seq[i])
                count = 0

        new_seq += '{}{}'.format(count + 1, seq[-1])

        return new_seq

    def countAndSay(self, n: int) -> str:
        seq = '1'
        for _ in range(n-1):
            seq = self.count_and_say_seq(seq)

        return seq
