
from typing import List


class Solution:
    def stockBuyAndSell(self, n : int, a : List[int]) -> int:
        # code here
        dp =[0]*2
        curr = [0]*2
        n = len(a)
        dp[0]=dp[1]= 0
    
        for ind in range(n-1,-1,-1):
            
                curr[1]= max(dp[0]-a[ind],dp[1])
                curr[0]= max(dp[1]+a[ind],dp[0])
                dp = curr
        return dp[1]



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        prices=IntArray().Input(n)
        
        obj = Solution()
        res = obj.stockBuyAndSell(n, prices)
        
        print(res)
        

# } Driver Code Ends