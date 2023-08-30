## 回顾与思考

方法一: 遍历二叉树
方法二: 二分查找+位运算(时间有限等待研究)

## 题解

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0

    def countNodes(self, root: Optional[TreeNode]) -> int:
        def traverse(self, root):
            if not root:
                return
            traverse(self, root.left)
            traverse(self, root.right)
            self.count += 1
        traverse(self, root)
        return self.count
```
