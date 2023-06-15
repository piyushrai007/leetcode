class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
    
        for char in s:
            if char in mapping:
            # Found a closing bracket
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
            # Found an opening bracket
                stack.append(char)
    
    # If the stack is empty, all brackets are matched
        return len(stack) == 0
                  