class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        for i in operations:
            if i == 'C':
                stack.pop()
            elif i == 'D':
                stack.append(2*stack[-1])
            elif i == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(i))
        return sum(stack)