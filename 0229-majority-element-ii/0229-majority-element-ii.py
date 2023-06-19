class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        cnt1 = 0
        cnt2 =0
        elt1 = -99999999999
        elt2 = -99999999999
        ls = []
        for i in range(n):
            if cnt1 == 0 and elt2 != nums[i]:
                cnt1 = 1
                elt1 = nums[i]
            elif cnt2 == 0 and elt1 != nums[i]:
                cnt2 = 1
                elt2 = nums[i]   
            elif nums[i] == elt1:
                cnt1 +=1
            elif nums[i] == elt2:
                cnt2 +=1
            else:
                cnt1 -=1
                cnt2-=1
        cnt1 = 0
        cnt2 =0
        for i in range(n):
            if elt1 == nums[i]:
                cnt1 +=1
            if elt2 == nums[i]:
                cnt2 +=1
        mini = int(n / 3) + 1
        if cnt1 >= mini:
            ls.append(elt1)
        if cnt2 >= mini:
            ls.append(elt2)       
        return ls
            
