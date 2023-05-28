#User function Template for python3

class Solution:
    def CamelCase(self,N,Dictionary,Pattern):
        #code here
        out = []
        m=0
        for i in Dictionary:
            k=""
            for j in i:
                if j.isupper():
                    k += j
                    m= len(k)
            for p in range(m):    
                if k[:p+1] == Pattern :
                    out.append(i)
            
        if out:
            out.sort()
            return out 
        else:
            out.append(-1)
            return out
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Dictionary=list(map(str,input().split()))
        Pattern=input()
        ob=Solution()
        ans=ob.CamelCase(N,Dictionary,Pattern)
        ans.sort()
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends