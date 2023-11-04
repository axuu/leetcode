## 思考

此题同 0118,
用代码的方式构建杨辉三角, 规律是: 先拿到当前行的上一行, 在上一行的左右两边加上 0, 构建两个新行, 把两个行两两相加, 就是当前行的值.
需要注意的是 rowIndex 代表的是 row 的索引, 比 numRows 少 1, 所以修改 i 的初始值为 0

## 题解

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [[1]]
        i = 0
        while i < rowIndex:
            last_row = result[-1]
            row1 = [0]+last_row
            row2 = last_row+[0]
            row = [a+b for a, b in zip(row1, row2)]
            result.append(row)
            i += 1
        return result.pop()
```
