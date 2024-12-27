import heapq  # Importing the heapq module for heap operations

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        Find the k-th largest element in an unsorted array.
        
        :type nums: List[int] - List of integers
        :type k: int - The rank of the largest element to find
        :rtype: int - The k-th largest element
        """
        heap = []  # Initialize an empty heap
        
        # Push all elements of nums into the heap as their negatives
        # to simulate a max-heap using Python's min-heap implementation
        for i in range(len(nums)):
            heapq.heappush(heap, -nums[i])
        
        top = 0  # Variable to store the k-th largest element
        
        # Extract the smallest (negative of the largest) element k times
        for i in range(k):
            top = heapq.heappop(heap)
        
        # Return the k-th largest element by negating the result
        return -top
