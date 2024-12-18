# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur =  cur.next
        k  = k % len(arr)

        if k == 0:
            return head
            
        arr= arr[-k:] + arr[:-k]
        dummy = ListNode()
        temp = dummy
        
        for val in arr:
            temp.next = ListNode(val)
            temp = temp.next
            
        return dummy.next
    
    