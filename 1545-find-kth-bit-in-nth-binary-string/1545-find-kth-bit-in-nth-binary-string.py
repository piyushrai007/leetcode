class Solution:
    def doing(self,x):
        z=""
        for i in x:
            if i=="1":
                z+="0"
            else:
                z+="1"
        z=z[::-1]
        return z
    
    def sol(self,n):
        if n == 1:
            return "0"
        else:
            x= self.sol(n-1)
            s = x+"1"+self.doing(x)
            return s
        
    
    def findKthBit(self, n: int, k: int) -> str:
        m = self.sol(n)
        print(m)
        return m[k-1]