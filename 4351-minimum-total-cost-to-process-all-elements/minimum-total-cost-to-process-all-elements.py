class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        total = sum(nums)
        amount = total - k
        if amount <= 0:
            return 0

        count = math.ceil(amount / k)
        total_cost = count * (count + 1) // 2
        return total_cost % (10 ** 9 + 7)
            
        """
        4-(1+2+3+4)
        =4-10
        =-6
        We need to get back to 0 by adding k=4 a bunch of times
        -6+x*4 will get you over 0
        -6+2*4 = 2
        
        
        yay
        total operations: 2
        total cost: 2(2+1)/2=3
        """
        


        """
        for n in nums:
            print("processing", n)
            if resources < n:
                amount = n - resources
                count = math.ceil(amount / k)
                resources += count * k
                operations += count
                
                print("amount", amount)
                print("count", count)
                print("adding resources", count * k)
                print("adding operations", count)

            resources -= n
            print("now we have resources=", resources)
            print()
            
        total_cost = operations * (operations + 1) / 2
        print("operations", operations)
        print("total cost", repr(total_cost))
        # 1+2+3+4+
        """