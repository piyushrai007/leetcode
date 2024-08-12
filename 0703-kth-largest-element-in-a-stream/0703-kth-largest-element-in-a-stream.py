class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # put first k elements.
        self.heap = nums[0:k]
        self.k = k
        heapq.heapify(self.heap)
        
        # check the rest of the array
        for x in nums[k:]:
            if self.heap[0] < x: heapq.heappushpop(self.heap, x)
        

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
            return self.heap[0]
        
        if self.heap[0] < val: heapq.heappushpop(self.heap, val)
        return self.heap[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)