def basso(a,ind,buy,dp):

    if ind == len(a):
        return 0
    if dp[ind][buy]!=-1:
        return dp[ind][buy]     
    if buy:
        profit = max(basso(a,ind+1,0,dp)-a[ind],basso(a,ind+1,1,dp))
    else:
        profit = max(basso(a,ind+1,1,dp)+a[ind],basso(a,ind+1,0,dp))
    dp[ind][buy] = profit
    
    return dp[ind][buy]
    
class Solution(object):
    
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[-1 for j in range(2)] for i in range(len(prices))]

        return basso(prices,0,1,dp)
        