## 思考

用了一个 Python 反转字符串的简单方法

和第 7 题一样，应该也可以用除 10 的方法来解

## 题解

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
```

