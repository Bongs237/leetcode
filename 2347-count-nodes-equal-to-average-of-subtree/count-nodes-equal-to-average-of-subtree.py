# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0 

        def summer(node):
            nonlocal ans

            subtree_sum = 0
            count = 0

            if not node:
                return 0, 0 # Dont even consider this thing
            elif not node.left and not node.right:
                subtree_sum = node.val
                count = 1
            else:
                left_sum, left_count = summer(node.left)
                right_sum, right_count = summer(node.right)

                subtree_sum = left_sum + right_sum + node.val
                count = left_count + right_count + 1

            avg = subtree_sum // count
            if node.val == avg:
                ans += 1

            return subtree_sum, count

        summer(root)

        return ans