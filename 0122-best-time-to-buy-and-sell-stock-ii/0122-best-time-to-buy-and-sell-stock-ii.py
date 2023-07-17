
    
class Solution(object):
    
    
    def maxProfit(self, a):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp =[0]*2
        curr = [0]*2
        n = len(a)
        dp[0]=dp[1]= 0

        for ind in range(n-1,-1,-1):

                curr[1]= max(dp[0]-a[ind],dp[1])
                curr[0]= max(dp[1]+a[ind],dp[0])
                dp = curr
        return dp[1]