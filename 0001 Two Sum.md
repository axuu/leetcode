## 回顾与思考

难点：Test case 中有很长的数组，可能会 Time Limit Exceeded

最开始想到的是双循环求解，觉得计算量太大，后来想到用双指针

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        while i < len(nums) - 1:
            if nums[i] + nums[j] == target:
                return [i, j]
            if (j == len(nums) - 1):
                i = i + 1
                j = i + 1
            else:
                j = j + 1
```

但仍然超时，参考 discuss 发现可以用 dict 保存遍历过的数据

需要注意：

- 遍历中如果需要获得 index，需要使用 enumerate()
- 和 JavaScript 不同，index 值在元素之前

## 题解

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, e in enumerate(nums):
            if target - e in d:
                return [i, d[target - e]]
            else:
                d[e] = i
```
