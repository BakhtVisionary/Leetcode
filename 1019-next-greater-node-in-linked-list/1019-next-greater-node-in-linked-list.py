# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        position = -1  # To track the position of the current node
        stack = []  # To keep track of nodes where the next larger value is not yet found
        answer = []  # List to store the next larger values

        while head:  # Traverse the linked list
            position += 1
            answer.append(0)  # Initialize the answer for the current position with 0

            # Process the stack: update answer for positions where head.val is the next larger value
            while stack and stack[-1][1] < head.val:
                idx, _ = stack.pop()
                answer[idx] = head.val

            # Push the current node's position and value onto the stack
            stack.append((position, head.val))

            # Move to the next node
            head = head.next

        return answer
