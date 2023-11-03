## 思考

用代码的方式构建杨辉三角, 规律是: 先拿到当前行的上一行, 在上一行的左右两边加上 0, 构建两个新行, 把两个行两两相加, 就是当前行的值.
边缘 case:
当前行是第一行, 直接返回[[1]]

## 题解

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        i = 1
        while i < numRows:
            last_row = result[-1]
            row1 = [0]+last_row
            row2 = last_row+[0]
            row = [a+b for a, b in zip(row1, row2)]
            result.append(row)
            i += 1
        return result
```
