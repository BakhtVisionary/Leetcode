class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        # Mapping of digits to letters
        digit_to_char = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        # Backtracking function to explore all combinations
        def backtrack(index, path):
            # Base case: If the path length equals the digits length, add to result
            if index == len(digits):
                combinations.append("".join(path))
                return

            # Get the characters corresponding to the current digit
            possible_chars = digit_to_char[digits[index]]
            for char in possible_chars:
                path.append(char)       # Choose a character
                backtrack(index + 1, path)  # Explore further
                path.pop()             # Backtrack

        combinations = []
        backtrack(0, [])
        return combinations

