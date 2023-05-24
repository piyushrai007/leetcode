#User function Template for python3

class Solution:
	def closedIslands(self, matrix, N, M):
		def dfs(x, y):
            if x < 0 or x >= N or y < 0 or y >= M or matrix[x][y] == 0:
                return
            matrix[x][y] = 0
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
        
        def fill(x, y):
            if x < 0 or x >= N or y < 0 or y >= M or matrix[x][y] != 1:
                return
            matrix[x][y] = 0
            fill(x+1, y)
            fill(x-1, y)
            fill(x, y+1)
            fill(x, y-1)

        # Fill land cells connected to boundary with water
        for i in range(N):
            fill(i, 0)
            fill(i, M-1)
        
        for j in range(M):
            fill(0, j)
            fill(N-1, j)

        count = 0

        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 1:
                    dfs(i, j)
                    count += 1

        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N, M = map(int,input().split())
        matrix = []
        for i in range(N):
            nums = list(map(int,input().split()))
            matrix.append(nums)
        obj = Solution()
        print(obj.closedIslands(matrix, N, M))
# } Driver Code Ends