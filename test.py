# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def printList(self, head):
        while head:
            print(head.val)
            head = head.next
        print("----")

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        l = head
        while (l and l.next):
            print('p1', head.val)
            print('p2', head.next.val)
            if (l.val == l.next.val):
                print('equal', head.val)
                head.next = head.next.next
            l = l.next
            self.printList(self, head)
        return head
    
h = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
Solution.deleteDuplicates(Solution, h)