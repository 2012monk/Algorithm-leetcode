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
    int result = 999999999;
    int prev = -999999999;
    public int minDiffInBST(TreeNode root) {
        if (root == null) return 0;
        if (root.left != null) minDiffInBST(root.left);
        result = Math.min(result, root.val - prev);
        prev = root.val;
        if (root.right != null) minDiffInBST(root.right);
        
        return result;
    }
}