# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         """
#         Initialize a binary tree node with a value and optional left and right children.
#         :param val: The value of the node (default is 0).
#         :param left: The left child node (default is None).
#         :param right: The right child node (default is None).
#         """
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        Perform an in-order traversal of a binary tree and return the values as a list.
        
        In-order traversal visits the left subtree, then the root node, and finally the right subtree.
        
        :type root: Optional[TreeNode]
        :rtype: List[int]
        :param root: The root node of the binary tree.
        :return: A list of integers representing the in-order traversal of the binary tree.
        """
        # Initialize an empty list to store the traversal result.
        res = []
        
        # Define a helper function for the in-order traversal.
        def inorder(root):
            """
            Recursively traverse the binary tree in in-order fashion.
            
            :param root: The current node being processed.
            """
            # Base case: if the current node is None, return immediately.
            if not root:
                return
            
            # Recursively traverse the left subtree.
            inorder(root.left)
            
            # Process the current node by appending its value to the result list.
            res.append(root.val)
            
            # Recursively traverse the right subtree.
            inorder(root.right)
        
        # Call the helper function starting from the root node.
        inorder(root)
        
        # Return the result list containing the in-order traversal.
        return res
