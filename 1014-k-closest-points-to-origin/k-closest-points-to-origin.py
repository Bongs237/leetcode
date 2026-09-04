import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x, y in points:
            # since it's a min heap we need to negate it
            data = (-(x*x + y*y), x, y)

            if len(heap) == k:
                heapq.heappushpop(heap, data)
            else:
                heapq.heappush(heap, data)

        return [(x, y) for dist, x, y in heap]