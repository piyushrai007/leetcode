class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) -1
        ans  = float('-inf')
        while l<r:
            if height[l] < height[r]:
                ans  = max(ans,height[l]*(r-l))
                l+=1
            else:
                ans  = max(ans,height[r]*(r-l))
                r-=1
        return ans           

                