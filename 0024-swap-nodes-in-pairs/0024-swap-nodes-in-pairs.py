# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy  = ListNode(0,head)
        curr = head
        prev = dummy
        while curr and curr.next:
            np = curr.next.next
            sec = curr.next
            
            sec.next = curr
            curr.next = np
            prev.next =  sec
            
            prev = curr
            curr = np
        return dummy.next
            
            
    