# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        slow = head
          
        while n != 0 and head:
            
            fast = fast.next
            n-=1
        if fast == None:
            head = head.next
            return head
        while fast.next:
            fast = fast.next
            slow = slow.next
        temp = slow.next
        slow.next = temp.next
        
        return head
            
            
            