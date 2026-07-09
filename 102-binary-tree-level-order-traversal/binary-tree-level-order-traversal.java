/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        if (root == null) return ans;
        
        LinkedList<TreeNode> q = new LinkedList<>();

        // to start off, you add the only node on the top level, the root
        q.addLast(root);
        while (!q.isEmpty()) {
            // EVERY TIME we get to this point of the loop,
            // all nodes of the current level we're traversing should be in the queue

            // therefore the size of the level = size of the queue
            // that's the trick
            int levelSize = q.size();

            List<Integer> currentList = new ArrayList<>();
            for (int i = 0; i < levelSize; i++) {
                // enqueue both of the children from each node on this level
                TreeNode item = q.peek();
                if (item.left != null) q.addLast(item.left);
                if (item.right != null) q.addLast(item.right);

                // add each node on this level to the list
                currentList.add(item.val);
                // kill each node on the current level
                q.removeFirst();
            }
            ans.add(currentList);
        }

        return ans;
    }
}