class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        
        v = s[::-1]
        if s == v:
            return True
        else:
            return False
        
            