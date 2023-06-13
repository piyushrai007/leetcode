class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for row in grid:
            for column in zip(*grid):
                arr = list(column)
                if row  == arr:
                    count +=1
        return count             
            
        