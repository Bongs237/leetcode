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

const sortedArrayToBST=r=>{if(!r.length)return null;let e=Math.floor(r.length/2),t=new TreeNode(r[e]);return t.left=sortedArrayToBST(r.slice(0,e)),t.right=sortedArrayToBST(r.slice(e+1)),t};