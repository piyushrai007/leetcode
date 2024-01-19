class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()  # Keep track of seen numbers to detect cycles
        while n not in seen:
            seen.add(n)
            sum_of_squares = 0
            while n > 0:
                digit = n % 10
                sum_of_squares += digit * digit
                n //= 10
            n = sum_of_squares
        return n == 1