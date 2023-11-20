## 思考

方法一:

判断一个链表是否存在循环, 使用单次遍历, 每遍历一个节点, 用一个标记来标记是否访问过, 如果访问过则存在循环, 否则不存在循环.

因为 ListNode 的结构已经给定, 无法修改, 所以通过修改 val 的值实现.

空间复杂度 O(1), 时间复杂度 O(n)

方法二 快慢指针:

首先想像我和朋友在一个圆形跑道上跑步. 如果跑道长 100 米, 我的速度是 10 米/秒, 朋友的速度是 5 米/秒. 那么 20 秒后，我跑了 200 米，朋友跑了 100 米. 但因为跑道是环形的, 所以我们会在同一个地方, 因为距离正好相差 100 米.

如果换一条跑道, 或者改变两个人的速度. 最后会发现, 只要你们的速度不一样, 速度快的人总会再次追上速度慢的人. 这就是这个问题的关键所在.

这种方法也被称为 "龟兔赛跑" 算法, 使用两个指针以不同的速度遍历列表. 慢指针每次移动一步, 而快指针则移动两步. 如果有一个循环, 快指针最终会赶上慢指针.

## 题解

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 方法一
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l = head
        while l:
            if (l.val == 'visited'):
                return True
            else:
                l.val = 'visited'
            l = l.next
        return False

# 方法二
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head
        fast_pointer = head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False
```
