class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        s=list(x)
        l=0
        r=len(s)-1

        while l<r:
            s[l],s[r]=s[r],s[l]

            l += 1
            r -= 1
        return "".join(s) == x