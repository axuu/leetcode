## 回顾与思考

这是一道初做的时候没有思路的题目, 因为单纯的循环依次比较节点不能解决问题, 可能会出现值相同但是节点不同的情况.

使用的技巧是将两个链表相互拼接, 然后从头开始遍历, 如果有相同的节点, 那么这个节点就是相交的节点, 感觉是一种数学的技巧.

Python 中比较两个指针是否是同一个指向, 可以使用 `is` 关键字. 否定的写法是 `is not`.

边缘 case:

1. 两个链表没有相交的情况, 两个链表都遍历完了, 但是没有相交的节点, 此时返回 p1 等于 None, 是没有问题的

## 题解

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        while p1 is not p2:
            if (p1 == None):
                p1 = headB
            else:
                p1 = p1.next
            if (p2 == None):
                p2 = headA
            else:
                p2 = p2.next
        return p1
```
