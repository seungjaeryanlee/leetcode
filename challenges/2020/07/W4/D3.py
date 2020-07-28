"""
Solution for July LeetCoding Challenges Week 4 Day 3: All Paths From Source to Target
"""
class Solution:
    """
    DFS recursion passing source and path up to the source. Inefficient since
    each path from the source to the destination must be calculated again for
    different paths to the source.

    Runtime: 160 ms / 19.07%
    Memory Usage: 15.8 MB / 5.93%
    """
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        destination = N - 1

        output = []
        def _path_from_source(source: int, path: List[int]):
            if source == destination:
                output.append(path.copy())
                return

            for neighbor in graph[source]:
                path.append(neighbor)
                _path_from_source(neighbor, path)
                path.pop()
        _path_from_source(0, [0])

        return output
