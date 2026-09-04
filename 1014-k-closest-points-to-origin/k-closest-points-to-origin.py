class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return [[x, y] for dist, x, y in (sorted([(x * x + y * y, x, y) for x, y in points])[:k])]