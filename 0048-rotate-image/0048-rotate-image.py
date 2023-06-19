class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        ans = [[None] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ans[j][(n-1)-i] = matrix[i][j]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = ans[i][j]