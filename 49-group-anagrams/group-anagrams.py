class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alpha = [["".join(sorted(s)), s] for s in strs]
        alpha.sort()

        ans = []
        curr = [ alpha[0][1] ]
        for i in range(1, len(alpha)):
            if alpha[i - 1][0] == alpha[i][0]:
                curr.append(alpha[i][1])
            else:
                ans.append(curr)
                curr = [ alpha[i][1] ]

        ans.append(curr)

        return ans