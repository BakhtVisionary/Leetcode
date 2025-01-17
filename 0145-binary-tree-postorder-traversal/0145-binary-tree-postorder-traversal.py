# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        
        def postorder(root):
            if not root:
                return 
            else :
                postorder(root.left)
                postorder(root.right)
                res.append(root.val)
        postorder(root)
        return res
                