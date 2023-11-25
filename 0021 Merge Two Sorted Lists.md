## 回顾与思考

方法一 递归:

最开始没有想明白循环应该怎样处理, 所以使用了递归. 每次比较两个链表的头结点(A 和 B), 如果 A 较小, 那么 A 作为返回值, 同时递归去比较 A.next 和 B. 反之, B 作为返回值, 同时递归去比较 A 和 B.next.

如果其中一个链表为空, 直接返回另一个链表的剩余结点.

方法二 循环:

创建一个虚拟头结点和一个 p 指针, 方便返回结果 dummy.next

比较 p1 和 p2 两个指针, 将值较小的的节点接到 p 指针

让 p 指针不断前进

如果其中一个链表为空, 直接将 p 指针指向另一个链表的剩余结点

## 题解

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 方法一 递归
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 == None):
            return list2
        if (list2 == None):
            return list1

        if list2.val >= list1.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

# 方法二 循环
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = dummy
        p1 = l1
        p2 = l2

        while p1 and p2:
            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next

        if p1:
            p.next = p1

        if p2:
            p.next = p2

        return dummy.next
```
