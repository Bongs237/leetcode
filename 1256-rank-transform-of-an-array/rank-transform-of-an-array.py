class Solution:
    def binary_search(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if target > arr[mid]:
                left = mid + 1
            elif target < arr[mid]:
                right = mid - 1
            else:
                return mid + 1

        return -1

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sorted = sorted(list(set(arr)))
        ans = []
        
        for i in range(len(arr)):
            rank = self.binary_search(arr_sorted, arr[i])
            ans.append(rank)

        return ans