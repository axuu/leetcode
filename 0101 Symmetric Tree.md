## 回顾与思考

参考了其他题解, 因为原函数只有一个参数 root, 递归时不方便传递参数. 使用的技巧是利用另一个函数, 把参数 root 变成了 left 和 right, 这样就可以用代码表达"对称"这个定义了.

边缘 case:

- left 和 right 二者都是 None, 对称
- left 和 right 二者只有一个是 None, 不对称
- 根节点如果是 None, 对称

## 题解

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
```
