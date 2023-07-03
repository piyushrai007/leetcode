class Solution(object):
    
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        else:
            words = s.split()
            return len(words[len(words)-1])       