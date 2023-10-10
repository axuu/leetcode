## 思考

此题实现起来比较简单, 计算两个位置之间元素的和即可, 但这样计算性能排名会比较低.

参考别人的回答, 可以在 class 初始化的时候, 提前计算出前 i 项的前缀和, 这样在计算区间和的时候, 只需要计算两个前缀和的差值即可.

## 题解

```python
# 方法一
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left, right + 1):
            sum += self.nums[i]
        return sum

# 方法二
def __init__(self, nums: List[int]):
    self.nums = nums
    self.pre = nums
    for i in range(len(self.pre) - 1):
        self.pre[i + 1] += self.pre[i]

def sumRange(self, left: int, right: int) -> int:
    self.left = left
    self.right = right
    if self.left:
        return self.pre[right] - self.pre[left - 1]
    else:
        return self.pre[right]
```
