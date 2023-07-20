def memo(a,ind,buy,cap,dp):
    if cap == 0:
        return 0
    if ind == len(a):
        return 0
    if dp[ind][buy][cap]!=-1:
        return dp[ind][buy][cap]
    if buy:
        dp[ind][buy][cap] = max(memo(a,ind+1,0,cap,dp)-a[ind],memo(a,ind+1,1,cap,dp))
    else:
        dp[ind][buy][cap]= max(memo(a,ind+1,1,cap-1,dp)+a[ind],memo(a,ind+1,0,cap,dp))
    return dp[ind][buy][cap]
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        t = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(len(prices))]
        return memo(prices,0,1,2,t)