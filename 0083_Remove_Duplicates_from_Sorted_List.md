## 思考

感受: 对指针的问题还是理解不够透彻

- 无需遍历到最后一个节点, 因为是当前节点和下一个节点比较, 只需要遍历到倒数第二个节点.
- 需要新创建一个 p 指针, 并且在循环中不断移动指针, 不能直接用 head, head 是用来返回结果的.
- 转移指针是 p = p.next, 检测到相同值之后覆盖节点是 p.next = p.next.next, 二者容易混淆

## 题解

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p and p.next:
            if (p.val == p.next.val):
                p.next = p.next.next
            else:
                p = p.next
        return head
```
