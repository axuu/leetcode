## 回顾与思考

方法一:

把链表记录成数组, 然后比较

时间复杂度: O(n)
空间复杂度: O(n)

方法二:

为了将空间复杂度从 O(n) 优化到 O(1)

- 首先使用循环检测, 找到中间的节点
- 借助另一个变量来反转列表的后半部分，该变量包含对前一个节点（prev）的引用和一个三向交换。在此之前，需要设置 prev.next = null，是为了避免出现循环
- 当后半部分正确反转，就可以同时重新开始遍历和比较前后两部分，不需要额外的空间。如果两个指针的值不一致，我们可以返回 false，否则，如果两个指针都成功到达中间，我们可以返回 true。

PS：无论链表的长度是奇数还是偶数，这个过程都会起作用

## 题解

```python
# 方法一:
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        p = head
        while p:
            l.append(p.val)
            p = p.next
        for i in range(len(l)):
            if (l[i] != l[len(l) - i - 1]):
                return False
        return True

# 方法二:
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 找到中点
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 反转后半部分
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev = prev, slow
            slow = slow.next

        # 比较前后两部分
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True
```
