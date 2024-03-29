# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum_exp):
        if root == None:
            return False
        if root.left == None and root.right == None:
            return root.val == sum_exp
        return self.hasPathSum(root.left, sum_exp - root.val) or self.hasPathSum(root.right, sum_exp - root.val)
    

