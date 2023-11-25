## 回顾与思考

经典的反转单链表

方法一 hashmap:

将链表中的值存入数组中, 然后反转数组, 最后用数组中的值构建一个新链表.

方法二 迭代:

初始化两个指针, prev 指向 None, curr 指向 head, 然后循环, 每次循环中:

1. 断开原链表的第一个节点, 其余(除了第一个节点)的部分保留到 next 中
2. curr.next = prev, 即每次都用当前的节点作为 head, prev 是后面的部分.
3. prev 指向 curr, curr 指向 next, 继续下个循环

方法三 递归:

初看有些不好理解.

首先看边缘 case: 如果链表为空或者只有一个节点, 那么返回的就是 head 本身.

递归先确定反转链表的返回值: 返回的是反转后的链表的头节点.

假定原链表 head.next 及后面部分已经反转好了, 下面就需要把新链表的尾巴和原链表的头接上, 恰好新链表的尾巴的指针是 head.next, 所以汤 head.next.next = head

最后链表的尾部要指向空, 所以 head.next = None, 这样就完成了反转.

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

# 方法三
class Solution:
    def reverseList(self, head):
        if (head == None or head.next == None):
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
```
