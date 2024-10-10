class Solution:
    def maxWidthRamp(self, nums):
        ans = 0
        n = len(nums)

        vp = [(nums[i], i) for i in range(n)]

        vp.sort()
        print(vp)

        min_index = vp[0][1]

        for i in range(1, n):
            current_index = vp[i][1]
            ans = max(ans, current_index - min_index)
            min_index = min(min_index, current_index)

        return ans
                
                
        