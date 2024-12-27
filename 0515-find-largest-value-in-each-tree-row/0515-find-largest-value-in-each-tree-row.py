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
        ans = []  # List to store the largest values of each row
        queue = deque()  # Queue for level-order traversal

        if root:
            queue.append(root)  # Add the root node to the queue

        while queue:
            largest = -2**31  # Reset largest to a very small value for each level
            for _ in range(len(queue)):  # Process all nodes at the current level
                node = queue.popleft()  # Remove the node from the queue
                largest = max(largest, node.val)  # Update the largest value for the level
                
                # Add left and right children to the queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(largest)  # Add the largest value of the level to the result

        return ans
