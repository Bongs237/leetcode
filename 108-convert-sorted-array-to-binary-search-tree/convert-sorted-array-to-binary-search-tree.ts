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

    const stack = [];
    let root;

    // [left, right, parent node, child type "left" or "right"]
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
        //console.log(leftRange, "left range");
        if (leftRange >= 1) stack.push([left, mid - 1, newNode, "left"]);

        // Compute range of right + push
        const rightRange = right - (mid + 1) + 1
        //console.log(rightRange, "right range");
        if (rightRange >= 1) stack.push([mid + 1, right, newNode, "right"]);

        //console.log(stack);
    }

    return root;
};