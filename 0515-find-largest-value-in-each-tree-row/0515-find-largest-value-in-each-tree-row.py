from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def largestValues(self, root):
        """
        Find the largest value in each row of a binary tree.
        
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []  # Early return if the tree is empty
        
        ans = []  # List to store the largest values of each row
        queue = deque([root])  # Initialize queue with the root node

        while queue:
            level_size = len(queue)  # Number of nodes in the current level
            largest = float('-inf')  # Initialize the largest value for the level
            
            for _ in range(level_size):
                node = queue.popleft()  # Process the current node
                largest = max(largest, node.val)  # Update the largest value
                
                # Add children to the queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(largest)  # Add the largest value of the level to the result

        return ans
