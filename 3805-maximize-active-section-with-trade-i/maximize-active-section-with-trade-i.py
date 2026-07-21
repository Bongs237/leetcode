class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        num_ones = 0
        for ch in s:
            if ch == '1':
                num_ones += 1

        st = []
        blocks = []

        # look for 0 1 0 blocks
        # 0 -> 1 -> 0
        # we find the number of 0's we're replacing with 1's
        
        for i in range(len(s)):
            # If the prev char != this char or it's the first character
            if (i > 0 and s[i - 1] != s[i]) or i == 0:
                if s[i] == '0':
                    #print(st)
                    if len(st) >= 2 and st[-1][0] == 1 and st[-2][0] == 0:
                        #print("We found a 0 1 0 at", i)
                        #print("starting", st[-2][1])
                        #print("ending", st[-1][1])

                        # store:
                        # start of 0s, start of 1s, end of 1s (start of next 0s), end of 0s
                        blocks.append([ st[-2][1], st[-1][1], i, -1 ])
                        st = []

                    st.append([0, i])
                elif s[i] == '1':
                    if st:
                        st.append([1, i])

            # Find the end of a 0 block
            # It's a 0, and it's at the end, or the char after this one is a 1
            if s[i] == '0' and (i == len(s) - 1 or (i < len(s) - 1 and s[i + 1] == '1')):
                if blocks:
                    # set end
                    blocks[-1][3] = i
                    start0, start1, end1, end0 = blocks[-1]
                    # then refactor so it only contains the number of 0's replaced
                    num_zero_left = start1 - start0
                    num_zero_right = end0 - end1 + 1
                    blocks[-1] = num_zero_left + num_zero_right

        #print(blocks)

        if not blocks:
            return num_ones

        return max(blocks) + num_ones
