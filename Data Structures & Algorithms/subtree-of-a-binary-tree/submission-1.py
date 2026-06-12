# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSameTree(self, p, q):
        if not p  and not q :
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)

        return False  

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        temp = root
        if not subRoot:
            return True
        if not temp:
            return False
        if self.isSameTree(temp, subRoot):
            return True
        return (self.isSubtree(temp.left, subRoot) or self.isSubtree(temp.right, subRoot))


        