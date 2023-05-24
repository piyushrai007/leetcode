# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        p = l1
        q = l2
        current = dummyHead
        carry = 0

        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            summation = x + y + carry
            carry = summation // 10
            current.next = ListNode(summation % 10)
            current = current.next
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummyHead.next
        
            