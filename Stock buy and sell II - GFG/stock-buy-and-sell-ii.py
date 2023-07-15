
from typing import List


class Solution:
    def stockBuyAndSell(self, n : int, a : List[int]) -> int:
        # code here
        dp = [[0 for j in range(2)] for i in range(len(prices)+1)]

        dp[n][0]=dp[n][1]= 0
    
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                if buy:
                    profit = max(dp[ind+1][0]-a[ind],dp[ind+1][1])
                else:
                    profit = max(dp[ind+1][1]+a[ind],dp[ind+1][0])
                dp[ind][buy] = profit
        
        return dp[0][1]



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