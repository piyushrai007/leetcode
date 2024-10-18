# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        nodes_seen = set()
        current = head
        while current:
            if current in nodes_seen:
                return True
            nodes_seen.add(current)
            current = current.next
        return False
