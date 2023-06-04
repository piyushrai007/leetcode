class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

    # Find the minimum length string in the array
        min_length = min(len(s) for s in strs)

    # Iterate over the characters up to the minimum length
        for i in range(min_length):
        # Check if all characters at position i are the same
            if not all(s[i] == strs[0][i] for s in strs):
                return strs[0][:i]  # Return the prefix up to position i

        return strs[0][:min_length] 