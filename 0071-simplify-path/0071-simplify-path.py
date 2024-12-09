class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        stack = []
        i = 0
        while i < len(path):
            if path[i] == '..':  # Check for parent directory
                if stack:
                    stack.pop()
            elif not (path[i] == '.' or path[i] == ''):  # Ignore '.' and empty strings
                stack.append(path[i])  # Add valid directory to the stack
            i += 1
        return '/' + '/'.join(stack)  # Construct and return the simplified path
