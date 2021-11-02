## 思考

两个阻碍思路的地方：

1. 考虑到所有边界条件
2. p.val == q.val 是不能返回 True 的，因为虽然两个节点相等，但他们的子节点不一定相等，需要继续遍历

```python
if p.val == q.val: # 这两行是不能写的
  return True
```

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
        if not p and not q:
          return True
        if (p and not q) or (q and not p):
          return False
        if p.val != q.val:
          return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

