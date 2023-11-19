## 回顾与思考

方法一:

把链表记录成数组, 然后比较

时间复杂度: O(n)
空间复杂度: O(n)

## 题解

```python
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
```
