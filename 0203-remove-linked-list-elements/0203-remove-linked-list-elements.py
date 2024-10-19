class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        temp = None
        temp2 = head

        while temp2 is not None:
            if temp2.val == val:
                if temp is None:
                    head = head.next
                    temp2 = head
                elif temp2.next is None:
                    temp.next = None
                    break
                else:
                    temp2 = temp2.next
                    temp.next = temp2
            else:
                temp = temp2
                temp2 = temp.next

        return head
