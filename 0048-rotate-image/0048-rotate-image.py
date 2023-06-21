class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n-1):
            for j in range(i+1,n):
                temp = matrix[i][j]
                matrix[i][j] =  matrix[j][i]
                matrix[j][i] = temp 
        for i in range(n):
            matrix[i].reverse()