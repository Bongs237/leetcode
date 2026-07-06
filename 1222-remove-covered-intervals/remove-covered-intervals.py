class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # merge intervals: electric boogaloo
        intervals.sort()
        print(intervals)

        # Remove the smaller interval in terms of size
        # larger in terms of interval[0]
        # [3,6] remove, keep [2,8]

        removed = []
        removed.append(intervals[0])

        for i in range(1, len(intervals)):
            # end of first >= end of last
            first = removed[-1]
            second = intervals[i]

            if first[1] >= second[1]:
                print("COVERED")
            elif second[1] >= first[1] and first[0] == second[0]:
                print("also covered")
                removed[-1] = second
            else:
                print("we're good")
                removed.append(second)

            print(first, second)
            
            print("removed=", removed)

        return len(removed)