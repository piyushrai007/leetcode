
class Solution(object):
    def func(self,node,graph,visited):
            visited[node]=0
            ans=1
            for i in graph[node]:
                if visited[i]==-1:
                    ans&=self.func(i,graph,visited)
                else:
                    ans&=visited[i]
            if ans==1:
                visited[node]=1
                return 1
            return 0
    def canFinish(self, numCourses,prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        graph=[[] for _ in range(numCourses)]
        for i,j in prerequisites:
            graph[j].append(i)
        visited=[-1]*numCourses
        for i in range(numCourses):
            if visited[i]==-1:
                if self.func(i,graph,visited)==0:
                    return False
        return True