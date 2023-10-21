## 思考

此题的设计比较简单, 因为 range 固定从 0 开始, 所以 i 的值, 就是元素应该有的值.

可以先对数组进行排序, 然后遍历数组, 遇到和 i 不相等的元素, 则返回 i.

需要注意, 如果遍历完数组都没有找到不相等的元素, 说明缺失值是最后一位, 返回数组长度即可.

## 题解

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if (nums[i] != i):
                return i
        return len(nums)
```
