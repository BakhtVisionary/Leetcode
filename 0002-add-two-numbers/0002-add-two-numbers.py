# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list1 = l1
        list2 = l2
        carry = 0
        dummy = ListNode()  # Dummy node to simplify edge cases
        temp = dummy  # Pointer to the current node in the result list
        
        while list1 or list2 or carry:  # Loop until no digits and no carry
            first = list1.val if list1 else 0  # Get value from list1 or 0
            second = list2.val if list2 else 0  # Get value from list2 or 0
            
            total = first + second + carry  # Sum the two values and the carry
            carry = total // 10  # Update carry
            digit = total % 10  # Get the current digit
            
            temp.next = ListNode(digit)  # Create new node for the current digit
            temp = temp.next  # Move the pointer forward
            
            if list1:  # Move to the next node in list1 if it exists
                list1 = list1.next
            if list2:  # Move to the next node in list2 if it exists
                list2 = list2.next
                
        return dummy.next  # Return the result list, skipping the dummy node
