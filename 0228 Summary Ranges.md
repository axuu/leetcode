## 回顾与思考

思路是遍历数组, 记录一个起始元素 start, 如果当前元素和下一个元素不连续(用 i 和 i + 1 判断), 则将当前元素和起始元素组成一个区间, 并将起始元素指向下一个元素.

需要注意: 因为需要计算 nums[i+1], i 会有越界情况, 但又不能限制 i 范围, 否则就会遍历不全. 所以需要在判断条件中检查 i 是否是最后一个元素.

## 题解

```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        start = 0
        i = 0
        while i < len(nums):
            if (i == len(nums) - 1 or nums[i + 1] != nums[i] + 1):
                if (start == i):
                    result.append(str(nums[start]))
                else:
                    result.append(str(nums[start]) + '->' + str(nums[i]))
                start = i + 1
            i += 1
        return result
```
