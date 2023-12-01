## 回顾与思考

这题使用了 targetSum 作为判断值的传递, 每次向下传递一次, 扣掉当前节点自身的值, 直到叶子节点.

判断叶子节点的条件: 如果当前节点的值等于 targetSum, 且没有左右子节点, 则返回 True.

## 题解

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if root.val == targetSum and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

```
