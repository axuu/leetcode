## 回顾与思考

方法一:

将链表中的值存入数组中, 然后反转数组, 最后用数组中的值构建一个新链表.

方法二 循环:

初始化两个指针, prev 指向 None, curr 指向 head, 然后循环, 每次循环中:

1. 断开原链表的第一个节点, 其余(除了第一个节点)的部分保留到 next 中
2. curr.next = prev, 即每次都用当前的节点作为 head, prev 是后面的部分.
3. prev 指向 curr, curr 指向 next, 继续下个循环

## 题解

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 方法一
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = dummy = ListNode()
        p2 = head
        l = []
        while p2:
            l.append(p2.val)
            p2 = p2.next
        l.reverse()
        for v in l:
            p1.next = ListNode(v)
            p1 = p1.next
        return dummy.next

# 方法二
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
```
