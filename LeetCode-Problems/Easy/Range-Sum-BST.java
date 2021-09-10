class Solution {
    public int rangeSumBST(TreeNode root, int low, int high) {
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(root);
        int sum = 0;
        while (!q.isEmpty()){
            TreeNode curr = q.poll();
            if (curr.val >= low && curr.val <= high){
                sum += curr.val;
            }
            if (curr.left != null){
                q.add(curr.left);
            }
            if (curr.right != null){
                q.add(curr.right);
            }
        }
        return sum;
    }
}
