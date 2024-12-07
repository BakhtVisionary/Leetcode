# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_odd_linked_list=ListNode(1000)
        dummy_even_linked_list=ListNode(100)
        odd_ptr =dummy_odd_linked_list
        even_ptr = dummy_even_linked_list
        
        i = 1
        
        while head :
            if i % 2 == 0:
                even_ptr.next =  head
                even_ptr = even_ptr.next
            else:
                odd_ptr.next = head
                odd_ptr = odd_ptr.next
                
            head= head.next
            i =i + 1
            
            
        even_ptr.next = None
        odd_ptr.next = dummy_even_linked_list.next        
        return dummy_odd_linked_list.next
        
        
        
        
        
        