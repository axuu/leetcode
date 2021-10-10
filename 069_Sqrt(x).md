## 思考

一开始的想法是依次计算整数的平方，当 i^2 < x < (i+1)^2 时，i 是平方根的整数部分，但实际执行结果太慢了，遇到两次 Time Limite Exceeded，微调通过后成绩也非常差：

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1: 
            return x
        i = 0
        while i <= x:
            if i * i <= x and (i + 1) * (i + 1) > x:
                return i
            i = i + 1
```

Runtime: 4492 ms, faster than 5.01% of Python3 online submissions for Sqrt(x).

Memory Usage: 14.4 MB, less than 7.41% of Python3 online submissions for Sqrt(x).

看讨论区理解二分查找的方法，可以减少无用运算

## 题解

```python
class Solution:
   def mySqrt(self, x):
        lo, hi = 0, x
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid > x:
                hi = mid - 1
            elif mid * mid < x:
                lo = mid + 1
            else:
                return mid
        return hi
```