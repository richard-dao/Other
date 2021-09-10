class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q = list()
        q.append(root)
        s = 0
        while (len(q) != 0):
            curr = q.pop(0)
            if (curr.val >= low and curr.val <= high):
                s = s + curr.val
            if (curr.left != None):
                q.append(curr.left)
            if (curr.right != None):
                q.append(curr.right)
        return s
