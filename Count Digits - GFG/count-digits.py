#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        # code here

        s = str(N)
        cnt = 0
        
        for i in s:
            if  int(i) > 0 and N%int(i) ==0:
                cnt +=1
        return (cnt)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends