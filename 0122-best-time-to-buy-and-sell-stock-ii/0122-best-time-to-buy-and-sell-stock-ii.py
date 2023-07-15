
    
class Solution(object):
    
    
    def maxProfit(self, a):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(a)
        dp = [[0 for j in range(2)] for i in range(n+1)]

        dp[n][0]=dp[n][1]= 0
    
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                if buy:
                    profit = max(dp[ind+1][0]-a[ind],dp[ind+1][1])
                else:
                    profit = max(dp[ind+1][1]+a[ind],dp[ind+1][0])
                dp[ind][buy] = profit
        
        return dp[0][1]