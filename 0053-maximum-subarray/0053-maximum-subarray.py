class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = -10000000000
        sum = 0
        for i in range(len(nums)):
            sum = sum +nums[i]
            if sum >max:
                max = sum
            if sum <0:
                sum =0
        return max     
            
        