class Solution:
    def isSimilarEven(self, row: list[int], k: int) -> bool:
        for i, num in enumerate(row):
            if num != row[(len(row)+i-k) % len(row)]:
                return False
            
        return True

    def isSimilarOdd(self, row: list[int], k: int) -> bool:
        for i, num in enumerate(row):
            if num != row[(len(row)+i+k) % len(row)]:
                return False
            
        return True

    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        for i, row in enumerate(mat):
            if i % 2 == 0 and not self.isSimilarEven(row, k):
                return False
            elif i % 2 == 1 and not self.isSimilarOdd(row, k):
                return False

        return True
