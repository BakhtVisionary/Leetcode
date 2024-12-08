class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = {'+', '-', '*', '/'}  # Set of operators for quick lookup

        for token in tokens:
            if token not in operators:
                stack.append(int(token))  # Push integer value to the stack
            else:
                b = stack.pop()  # The second operand
                a = stack.pop()  # The first operand
                evaluation = self.evaluate(a, b, token)  # Pass the operator directly
                stack.append(evaluation)

        return stack[0]

    def evaluate(self, a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            # Use int() to perform flooring division in Python
            return int(a / b) if a * b >= 0 else -(-a // b)
        else:
            return None
