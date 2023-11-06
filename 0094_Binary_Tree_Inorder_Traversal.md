## 思考

二叉树中序遍历，本来比较简单，但题目要求记录下遍历的路径到一个数组，因为不能让每次执行函数时新建一个数组，所以难点在于维护一个函数定义域之外的数组。可以在函数中声明一个新函数。

144、145 前序、后序遍历同理

## 题解

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
      def exec(root: TreeNode):
        if not root:
          return None
        exec(root.left)
        r.append(root.val)
        exec(root.right)
      r = []
      exec(root)
      return r
```

