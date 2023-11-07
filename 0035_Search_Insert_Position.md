## 思考

1. 需要考虑到 target 和被比较元素相等的情况. 此时插入的位置应该是被比较元素的前边, 所以大于时不能有 =.
2. 考虑边缘情况, 即 target 小于数组中最小的元素, 或者大于数组中最大的元素.
3. 遍历的 i 范围应该是数组长度减 1, 否则会出现数组溢出的情况.

## 题解

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if (target <= nums[0]):
            return 0
        i = 0
        while i < len(nums) - 1:
            if (target > nums[i] and target <= nums[i+1]):
                return i + 1
            i += 1
        return i + 1
```
