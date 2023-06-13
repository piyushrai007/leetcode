#User function Template for python3

class Solution:
    def nthFibonacci(self, n):
        # code here 
        count = [None]*n
        for i in range(n):
            if i <2:
                count[i]= 1
            else:
                count[i]  = count[i-1]+count[i-2]
        return count[n-1]%1000000007
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.nthFibonacci(n))
# } Driver Code Ends