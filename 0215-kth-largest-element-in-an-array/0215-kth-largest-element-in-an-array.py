import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        
        for i in range(len(nums)):
            heapq.heappush(heap,-nums[i])
            
        top=0
        for i in range(k):
            top = heapq.heappop(heap)
            
        return -top