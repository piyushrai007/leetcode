#User function Template for python3
import re
class Solution:
    def reverseEqn(self, s):
        # code here
           # Split the string into individual numbers and operators
        parts = re.findall(r'\d+|[-+*/]', s)

    # Reverse the list of numbers and operators
        reversed_parts = parts[::-1]

    # Combine the reversed list into a single string
        reversed_equation = ''.join(reversed_parts)

        return reversed_equation
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends