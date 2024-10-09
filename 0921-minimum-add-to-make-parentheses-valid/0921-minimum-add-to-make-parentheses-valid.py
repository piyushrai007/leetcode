class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = 0
        b = 0
        for i in s:
            if i == '(':
                a += 1
            else:
                if a > 0:
                    a -= 1
                else:
                    b += 1
        return a + b
            