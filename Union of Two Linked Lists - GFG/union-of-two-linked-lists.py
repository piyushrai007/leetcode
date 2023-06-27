#User function Template for python3

class Solution:
    def union(self, head1,head2):
        # code here
        # return head of resultant linkedlist
        distinct_set = set()

    # Traverse the first linked list and add elements to the set
        current = head1
        while current is not None:
            distinct_set.add(current.data)
            current = current.next

    # Traverse the second linked list and add elements to the set
        current = head2
        while current is not None:
            distinct_set.add(current.data)
            current = current.next

    # Convert the set into a sorted list
        distinct_list = sorted(list(distinct_set))

    # Create a new linked list using the sorted list of distinct elements
        new_head = None
        current = None
        for data in distinct_list:
            if new_head is None:
                new_head = Node(data)
                current = new_head
            else:
                current.next = Node(data)
                current = current.next
    
        return new_head
                
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    for _ in range(int(input())):
        
        n1 = int(input())
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)
        
        n2 = int(input())
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        
        ob = Solution()
        printList(ob.union(ll1.head,ll2.head))
        print()

# } Driver Code Ends