# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTree(self, root):
        if root == None:
            return 0

        leftheight = self.binaryTree(root.left)
        if leftheight == -1:
            return -1
        rightheight = self.binaryTree(root.right)

        if rightheight == -1:
            return -1

        if abs(leftheight - rightheight) > 1:
            return -1
        return max(leftheight, rightheight) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root != None:
            if self.binaryTree(root) != -1:
                return True
            else:
                return False
            
        else:
            return True