
def heapify(arr,n,i):
    largest = i
    left = 2*i
    right = 2*i +1
    if left <=n and arr[largest]<arr[left]:
        largest = left
    if right <=n and arr[largest]<arr[right]:
        largest = right   
    if largest!=i:
        temp = arr[largest]
        arr[largest]= arr[i]
        arr[i]=temp    
        heapify(arr,n,largest)
class Solution(object):
   
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(nums)