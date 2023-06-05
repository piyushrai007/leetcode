class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
         # Convert x to string and handle the sign
        sign = -1 if x < 0 else 1
        x_str = str(abs(x))

    # Reverse the string of digits
        reversed_str = x_str[::-1]

    # Convert the reversed string back to an integer
        reversed_int = int(reversed_str) * sign

    # Check if the reversed integer is within the 32-bit range
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
        else:
            return reversed_int
        
        
            