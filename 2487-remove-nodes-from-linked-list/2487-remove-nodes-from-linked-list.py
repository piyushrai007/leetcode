# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(head):
    ptr = head
    prev = None 
    while ptr:
        temp = ptr.next
        ptr.next =  prev
        prev = ptr
        ptr =  temp
    return prev

class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = reverse(head)
        
        ptr  =  head.next
        ctr  =  head
        maxx = head.val
        while ptr:
            if ptr.val < maxx:
                ctr.next = ptr.next
            else:
                ctr = ptr
                maxx = ptr.val
            ptr = ptr.next
        return reverse(head)


                
                