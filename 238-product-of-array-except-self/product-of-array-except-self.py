class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        everything = 1
        zeroes = 0
        for num in nums:
            if num != 0:
                everything *= num
            else:
                zeroes += 1
        
        res = []
        for num in nums:
            if num == 0:
                if zeroes == 1:
                    res.append(everything)
                else:
                    res.append(0)
            else:
                if zeroes > 0:
                    res.append(0)
                else:
                    res.append(everything // num)

        return res