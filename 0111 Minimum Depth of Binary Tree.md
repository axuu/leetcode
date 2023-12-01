## 回顾与思考

本题很容易构建出 minDepth(root) = min(minDepth(root.left), minDepth(root.right)) + 1 的递归关系

但这个递归关系有一个问题, 就是如果 root.left 或者 root.right 有一个是 None, 那么为 None 的那个子树的其实并不应该参与比较, 因为它的深度是 0, 但是这个递归关系会把它当成 1, 这样就会导致结果错误.

## 题解

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if None in [root.left, root.right]:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
```
