#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        qe = []
        qe.append(0)
        vis = [0]*V
        vis[0] = 1
        ans = []
        while qe:
            node  = qe[0]
            qe.pop(0)
            # qe.pop()
    
            ans.append(node)
            for k in adj[node]:
                if vis[k] !=1:
                    vis[k]=1
                    qe.append(k)
        return ans


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends