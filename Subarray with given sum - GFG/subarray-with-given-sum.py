#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code 
        start=0
        curr=0
        for end in range(0,n):
            curr=curr+arr[end]
            
            # print(start ,end)
            while curr>s:
                curr=curr-arr[start]
                start=start+1
            
            if curr==s  and start<=end:
                # print(start ,end)
                return [start+1, end+1]
            
        return [-1] 
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends