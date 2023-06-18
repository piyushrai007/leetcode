#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        # Size of the given list
        n = len(A)

    # Declaring a hashtable
        hashtable = {}

    # Storing the elements with their occurrence
        for num in A:
            if num in hashtable:
                hashtable[num] += 1
            else:
                hashtable[num] = 1

    # Searching for the majority element
        for key, value in hashtable.items():
            if value > (n / 2):
                return key

        return -1   
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends