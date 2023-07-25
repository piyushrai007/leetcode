class Solution(object):
    def maxProfit(self,a):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(a)
        after = [[0 for _ in range(3)] for _ in range(2)]
        cur = [[0 for _ in range(3)] for _ in range(2)]
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range (1,3):
                    if buy:
                        cur[buy][cap] = max(after[0][cap]-a[ind],after[1][cap])
                    else:
                        cur[buy][cap] = max(after[1][cap-1]+a[ind],after[0][cap])
            after = cur
        return after[1][2] 