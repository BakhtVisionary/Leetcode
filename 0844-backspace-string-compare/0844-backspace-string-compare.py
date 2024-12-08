class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_stack = []
        t_stack = []
        for i in s:
            if i == '#':
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(i)
            
    
        for i in t:
            if i == '#':
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(i)
        
        
        if s_stack == t_stack:
            return True
        else:
            return False
        