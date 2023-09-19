class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        
        """
        dequeue = []
        ans = []
        n = len(nums)
        for i in range(n):
            if dequeue and dequeue[0] == (i -k ):
                dequeue.pop(0)
            while dequeue and nums[dequeue[-1]] < nums[i]:
                dequeue.pop(-1)  
            dequeue.append(i)
            if  i >= k-1:
                ans.append(nums[dequeue[0]])     
        return ans     
            
              
                
                           
                           
                