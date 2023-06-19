#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        sum_dict = {}
    
        # Initialize variables
        max_length = 0
        cumulative_sum = 0
    
        # Traverse the array and compute the cumulative sum
        for i in range(n):
            cumulative_sum += arr[i]
        
        # If cumulative sum is 0, update the max_length
            if cumulative_sum == 0:
                max_length = i + 1
        
        # If cumulative sum is already present in the dictionary, update the max_length
            if cumulative_sum in sum_dict:
                max_length = max(max_length, i - sum_dict[cumulative_sum])
            else:
            # Store the cumulative sum and its index in the dictionary
                sum_dict[cumulative_sum] = i
    
        return max_length






 

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends