/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function sortedArrayToBST(nums: number[]): TreeNode | null {
    // Strat: Keep picking the mid and then add the mid of the left and right sublists
    function addMid(left: number, right: number) {
        // They the same thing
        if (right == left) {
            return new TreeNode(nums[right]);
        } else if (right - left + 1 < 1) {
            return null;
        }

        const mid = left + Math.floor((right - left) / 2);
        let node = new TreeNode(nums[mid]);

        node.left = addMid(left, mid - 1);
        node.right = addMid(mid + 1, right);

        return node;
    }

    const root = addMid(0, nums.length - 1);

    return root;
};