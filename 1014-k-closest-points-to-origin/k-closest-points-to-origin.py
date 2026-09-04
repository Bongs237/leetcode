class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return [[x, y] for dist, x, y in (sorted([(math.sqrt(x ** 2 + y ** 2), x, y) for x, y in points])[:k])]