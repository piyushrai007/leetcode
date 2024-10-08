class Solution(object):
    def minSwaps(self, s):
        
        a=[]
        for i in s:
            if i=="[":
                a.append(i)
            elif i=="]":
                if len(a):
                    a.pop()
                
      
            
        n= len(a)
        if n%2 ==0:
            return n/2
        else:
            return (n+1)/2