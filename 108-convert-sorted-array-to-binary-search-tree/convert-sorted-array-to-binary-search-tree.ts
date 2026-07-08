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
    // Ugly iterative method
    const stack = [];
    let root;

    // Structure: [left, right, parent node, child type "left" or "right"]
    stack.push([0, nums.length - 1, null, null]);

    while (stack.length != 0) {
        const [left, right, parent, childType] = stack.pop();
        // Add to bst
        const mid = left + Math.floor((right - left) / 2);

        const newNode = new TreeNode(nums[mid]);
        if (parent == null) {
            // Set the root
            root = newNode;
        } else if (childType == "left") {
            parent.left = newNode;
        } else { // right
            parent.right = newNode;
        }

        // Compute range of left + push
        const leftRange = (mid - 1) - left + 1;
        if (leftRange >= 1) stack.push([left, mid - 1, newNode, "left"]);

        // Compute range of right + push
        const rightRange = right - (mid + 1) + 1
        if (rightRange >= 1) stack.push([mid + 1, right, newNode, "right"]);
    }

    return root;
};