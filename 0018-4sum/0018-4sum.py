class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        st = set()

        # checking all possible quadruplets:
        for i in range(n):
            for j in range(i+1, n):
                hashset = set()
                for k in range(j+1, n):
                    # taking bigger data type to avoid integer overflow:
                    sum_ = nums[i] + nums[j] + nums[k]
                    fourth = target - sum_
                    if fourth in hashset:
                        temp = [nums[i], nums[j], nums[k], fourth]
                        temp.sort()
                        st.add(tuple(temp))
                    # put the kth element into the hashset:
                    hashset.add(nums[k])

        ans = [list(t) for t in st]
        return ans
                    