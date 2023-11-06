## 思考

第一次做这个题想到的是数字转字符串的方法，但效率肯定是不高的，这次采用数学上循环除以 10 的方法

需要注意：反转后的数如果超过 32bit 的整数，返回 0，第一次提交没有考虑到这一点。

学到一个操作，很秀但可读性不强：

```python
sign = [1,-1][x < 0]
# 等价于
sign = -1 if x < 0 else 1
```

## 题解

```python
class Solution:
    def reverse(self, x: int) -> int:
        isPositive = x > 0
        if x < 0:
            x = -x
        r = 0
        while x > 0:
            n = x % 10 # 余数
            r = r * 10 + n
            if r > 2 ** 31 - 1:
                return 0
            x = x // 10
        return r if isPositive else -r
```

数字转字符串再反转方法的题解：

[bit_length()](https://python-reference.readthedocs.io/en/latest/docs/ints/bit_length.html)

```python
class Solution:
    def reverse(self, x: int) -> int:
        rev = int(str(abs(x))[::-1])
        return (-rev if x < 0 else rev) if rev.bit_length() < 32 else 0
```

