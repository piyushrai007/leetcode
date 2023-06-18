#User function Template for python3

class Solution:
    def UncommonChars(self,A, B):
        #code here
        a =""
        for i in A:
            if i not in B:
                a+=i
                    
        for j in B:
            if j not in A:
                a+=j
        a = ''.join(sorted(set(a)))
        if not a:
            return -1
        return a
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))

# } Driver Code Ends