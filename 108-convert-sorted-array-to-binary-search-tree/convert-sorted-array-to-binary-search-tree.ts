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
    function addMid(left: number, right: number) {
        if (right - left + 1 == 1) {
            return new TreeNode(nums[right]);
        }

        if (right - left + 1 < 1) {
            console.log("You don't gotta add it, return~");
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