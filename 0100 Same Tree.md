## 回顾与思考

拆分递归问题: 一个节点下面的树相等, 就是二者值相等, 且左右子树也相等

边缘情况: 二者都是 None, 也相等, `p is q` 可以用来判断二者是否都是 None

## 题解

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (p and q):
          return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
```
