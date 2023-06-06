class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        srr =  sorted(arr)
        i = 0
        a= srr[1]-srr[0]
        for j in range (1,len(srr)):
            if (srr[j] - srr[i]) != a:
                return False
            i+=1 
        return True     
                
            