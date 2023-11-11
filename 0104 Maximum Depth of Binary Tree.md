## 回顾与思考

用正常的递归思路, 把问题拆分为: 一个节点下面的最大深度, 等于左子树的最大深度和右子树的最大深度中较大的值.

注意:

- 递归的终止条件是节点为空, 返回 0, 且不需要判断 root.left == None and root.right == None, 只判断本身即可
- 最后的结果要加上根节点本身 1

## 题解

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (root == None):
            return 0
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        return left_max + 1 if left_max > right_max else right_max + 1

```
