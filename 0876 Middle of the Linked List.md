## 回顾与思考

这道题比较简单, 因为方法已经在之前的链表题中包含了.

快慢两个指针, 快指针每次走两步, 慢指针每次走一步, 当快指针走到头时, 慢指针刚好走到中间.

## 题解

```python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```
