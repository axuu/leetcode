## 回顾与思考

定义: 「平衡二叉树 balanced binary tree」中任意节点的左子树和右子树的高度之差的绝对值不超过 1。

计算任意一个二叉树节点 p 的高度:

- 如果 p 是 None, 返回 0.
- 递归的计算左右子树的高度, 取较大值, 加上本身的高度 1, 即 `max(self.height(p.left), self.height(p.right)) + 1`

利用 height 函数来实现题意, 如果是一个平衡二叉树, 则满足:

- 左右子树的高度差的绝对值不超过 1
- 左右子树也是平衡二叉树

## 题解

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if (root is None):
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return abs(self.height(root.left) - self.height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
```
