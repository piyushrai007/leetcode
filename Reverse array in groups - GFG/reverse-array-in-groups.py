#User function template for Python

class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, K):
		# code here
		start = 0

        for i in range(N):
            if (i + 1) % K == 0 or i == N - 1:
                # Reverse the subarray from start to i
                left = start
                right = i

                while left < right:
                    arr[left], arr[right] = arr[right], arr[left]
                    left += 1
                    right -= 1

                start = i + 1
        return arr        

#{ 
 # Driver Code Starts
#Initial template for Python

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()




# } Driver Code Ends