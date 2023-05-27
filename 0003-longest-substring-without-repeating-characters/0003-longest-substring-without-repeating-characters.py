class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        test = ""
        # Result
        maxLength = -1
     
        # Return zero if string is empty
        if (len(s) == 0):
            return 0
        elif(len(s) == 1):
            return 1
        for c in list(s):
            current = "".join(c)
         
        # If string already contains the character
        # Then substring after repeating character
            if (current in test):
                test = test[test.index(current) + 1:]
            test = test + "".join(c)
            maxLength = max(len(test), maxLength)
        return maxLength        
        