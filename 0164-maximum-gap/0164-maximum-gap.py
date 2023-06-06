class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a =  float('-inf')
        i =0
        l = len(nums)
        nums =  sorted(nums)
        if l<2:
            return 0
        for j in range(1,l):
            a = max(a,nums[j]-nums[i])
            i+=1
        return a     