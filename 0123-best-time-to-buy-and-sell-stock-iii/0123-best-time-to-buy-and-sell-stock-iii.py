import numpy as np
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
        size_dim1 = len(prices)
        size_dim2 = 2
        size_dim3 = 3

        t = np.full((size_dim1, size_dim2, size_dim3), -1)

        return int(memo(prices,0,1,2,t))