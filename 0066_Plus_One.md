## 思考

思路是先把数组转换成字符串, +1 然后再拆分.

注意利用 Python 的数组推导式语法

## 题解

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i, e in enumerate(digits):
            num += e * (10 ** (len(digits) - i -1))
        num += 1
        return [int(i) for i in str(num)]
```
