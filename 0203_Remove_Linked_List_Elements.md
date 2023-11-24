## 回顾与思考

做了几道链表之后这道比较简单了, 需要注意每次循环中断开原链表的连接.

## 题解

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        p1 = dummy = ListNode()
        p2 = head
        while p2:
            if (p2.val != val):
                p1.next = p2
                p1 = p1.next
            temp = p2.next
            p2.next = None
            p2 = temp
        return dummy.next
```
