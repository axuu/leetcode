## 回顾与思考

整体的思路没问题, 新建两个链表, 遍历原链表, 依次把节点关联到新的链表上.

几个关键点:

1. 不能用 p = p.next 直接让 p 指针前进，而是要断开原链表中的每个节点的 next 指针, 否则会出现循环. 总结起来就是, 如果我们需要把**原链表的节点**接到**新链表**上，而不是 new 新节点来组成新链表的话，那么断开节点和原链表之间的链接可能是必要的。那其实我们可以养成一个好习惯，但凡遇到这种情况，就把原链表的节点断开，这样就不会出错了。
2. 最后在拼接两个链表的时候, 要注意使用正确的指针, 最后一个循环后 p 是 None, 所以 l1 是最后一个节点, 所以用 l1.next 等于后边整个链表的头节点 nummy2.next.
3. 最后返回的也应该是正确的指针, 即 nummy1.next.

## 题解

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l1 = nummy1 = ListNode()
        l2 = nummy2 = ListNode()
        p = head
        while p:
            if (p.val < x):
                l1.next = p
                l1 = l1.next
            else:
                l2.next = p
                l2 = l2.next
            # 核心是断开链表, 否则会出现循环
            temp = p.next
            p.next = None
            p = temp
        l1.next = nummy2.next
        return nummy1.next
```
