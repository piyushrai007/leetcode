class Solution:
    def makeFancyString(self, s: str) -> str:
        result = ''
        for char in s:
            if not result[-2:] == char * 2:
                result += char
        return result