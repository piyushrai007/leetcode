class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
    
    # Use two pointers: one to track the current unique element and the other to iterate through the array
        unique = 0
    
        for i in range(1, len(nums)):
            if nums[i] != nums[unique]:
                unique += 1
                nums[unique] = nums[i]
    
        return unique + 1