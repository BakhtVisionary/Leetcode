class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []  # List to store all combinations

        # Helper function to perform backtracking
        def backtrack(start, comb):
            # Base case: If the current combination has `k` elements, add it to the results
            if len(comb) == k:
                res.append(comb[:])  # Use slicing to append a copy of the current combination
                return 
            
            # Iterate through the numbers from `start` to `n`
            for i in range(start, n + 1):
                comb.append(i)  # Add the current number to the combination
                backtrack(i + 1, comb)  # Recurse with the next number
                comb.pop()  # Remove the last number to backtrack and explore other combinations

        # Initialize the backtracking process
        backtrack(1, [])
        return res

# Example Usage:
