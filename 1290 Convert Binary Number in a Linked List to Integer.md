## 回顾与思考

自己的思路: 先获取链表深度, 然后一次遍历链表, 每次遍历时, 用深度减一次方, 乘以当前节点的值, 累加到结果中.

时间复杂度: O(n)
空间复杂度: O(1)

更简洁的做法: 一次遍历之后, 每次遍历时, 将结果乘以 2, 然后加上当前节点的值.

时间复杂度: O(n)
空间复杂度: O(1)

## 题解

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 方法一
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        deep = 0
        p = head
        while p:
            deep += 1
            p = p.next
        result = 0
        while head:
            result += pow(2, deep - 1) * head.val
            deep -= 1
            head = head.next
        return result

# 方法二
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answer = 0
        while head:
            answer = 2*answer + head.val
            head = head.next
        return answer
```
