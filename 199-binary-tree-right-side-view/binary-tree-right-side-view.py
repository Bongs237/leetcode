# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = deque()
        queue.append(root)

        ans = []

        while queue:
            #curr_level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                #curr_level.append(curr.val)

                #print(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            ans.append(curr.val)

        return ans