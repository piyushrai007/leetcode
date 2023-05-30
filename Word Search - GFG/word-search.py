class Solution:
	def isWordExist(self, board, word):
		#Code here
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(row, col, index):
        # Check if the word is found
            if index == len(word):
                return True

        # Check if the current position is within the board's boundaries
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

        # Check if the current position has been visited or does not match the word's character
            if visited[row][col] or board[row][col] != word[index]:
                return False

        # Mark the current position as visited
            visited[row][col] = True

        # Recursive DFS on the adjacent positions (up, down, left, right)
            if (
                dfs(row - 1, col, index + 1)
                or dfs(row + 1, col, index + 1)
                or dfs(row, col - 1, index + 1)
                or dfs(row, col + 1, index + 1)
            ):
                return True

        # Backtrack by marking the current position as unvisited
            visited[row][col] = False

            return False

    # Iterate through each cell in the board to start the search
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False

                    

#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for tt in range(T):
		n, m = map(int, input().split())
		board = []
		for i in range(n):
			a = list(input().strip().split())
			b = []
			for j in range(m):
				b.append(a[j][0])
			board.append(b)
		word = input().strip()
		obj = Solution()
		ans = obj.isWordExist(board, word)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends