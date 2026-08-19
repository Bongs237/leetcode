class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        tx, ty = target

        def manhattan(tx, ty, dx, dy):
            return abs(dx - tx) + abs(dy - ty)

        min_dist = 101
        ans = -1

        for i, drone in enumerate(drones):
            dx, dy, range = drone

            dist = manhattan(tx, ty, dx, dy)
            if dist > range:
                continue
            
            if dist < min_dist:
                min_dist = dist
                ans = i

        return ans
            