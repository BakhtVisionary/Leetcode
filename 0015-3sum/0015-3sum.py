class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Step 1: Sort the input array to enable two-pointer approach
        nums.sort()
        n = len(nums)
        ans = []  # List to store the resulting triplets
        
        # Step 2: Iterate through the array
        for i in range(n):
            # If the current number is positive, no three numbers can sum to 0
            if nums[i] > 0:
                break 
            
            # Skip duplicate numbers to avoid duplicate triplets in the result
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Step 3: Initialize two pointers
            low, high = i + 1, n - 1
            
            # Step 4: Use two-pointer technique to find valid triplets
            while low < high:
                total = nums[i] + nums[low] + nums[high]
                
                # Case 1: If the sum is 0, we found a triplet
                if total == 0:
                    ans.append([nums[i], nums[low], nums[high]])
                    
                    # Move both pointers to find other potential triplets
                    low += 1
                    high -= 1
                    
                    # Skip duplicate values for `low`
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    
                    # Skip duplicate values for `high`
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                
                # Case 2: If the sum is less than 0, move the `low` pointer to the right
                elif total < 0:
                    low += 1
                
                # Case 3: If the sum is greater than 0, move the `high` pointer to the left
                else:
                    high -= 1
        
        # Step 5: Return the list of triplets
        return ans
