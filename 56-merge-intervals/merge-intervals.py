class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # This will sort the array of arrays lexicographically
        # e.g. compare first element, then compare second, then ...

        # But we really want it to sort by the first element and this does the trick
        intervals.sort()

        ans = []

        i = 0
        for interval in intervals:
            # Then since it's sorted, we can apply THE HACK:
            # if the end of the first goes over the start of the second interval, then merge that thingy baby

            if not ans or ans[-1][1] < interval[0]:
                # Add the first interval by default
                # Avoid doing two pointers or some weird stuff by just adding the intervals that dont overlap
                # and then when they do, merge the current + last interval by modifying the last interval
                ans.append(interval)
            else:
                left = ans[-1][0]
                right = max(ans[-1][1], interval[1])
                merged = [left, right]
                ans[-1] = merged

        return ans