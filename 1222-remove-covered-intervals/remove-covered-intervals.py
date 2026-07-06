class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # merge intervals: electric boogaloo
        intervals.sort()

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
                # covered, dont include the second one
                pass
            elif second[1] >= first[1] and first[0] == second[0]:
                # covered, where you got intervals that are like
                """
                first  ------
                second ---------------
                """
                removed[-1] = second
            else:
                removed.append(second)

        return len(removed)