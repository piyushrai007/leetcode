class Solution(object):
    def merge(self, arr):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        arr.sort()
        lst = []
        for i in range(len(arr)):
            if len(lst) == 0 or arr[i][0] > lst[-1][-1]:
                lst.append(arr[i])
            if arr[i][0] <= lst[-1][-1] and arr[i][1]>=lst[-1][-1] :
                lst[-1][-1]= arr[i][1]
        
        return lst