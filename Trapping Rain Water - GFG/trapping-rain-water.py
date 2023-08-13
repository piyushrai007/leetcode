
class Solution:
    def trappingWater(self, height,n):
        #Code here
        l =0
        r= n-1
        trap =0 
        left_max= 0
        right_max =0
        while l<=r:
            if height[l]<=height[r]:
                if height[l]>=left_max:
                    left_max = height[l]
                else:
                    trap += (left_max -height[l])
                l +=1      
            else:
                if height[r]>=right_max:
                    right_max = height[r]
                else:
                    trap += (right_max -height[r])
                r-=1    
        return trap  

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends