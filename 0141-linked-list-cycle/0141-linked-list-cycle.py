# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next  # slow moves 1 step
            fast = fast.next.next  # fast moves 2 steps

            if slow == fast:
                return True  # cycle detected

        return False  # no cycle
        