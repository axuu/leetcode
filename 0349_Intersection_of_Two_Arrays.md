## 思考

寻找两个数组的交集, 要求结果中的每个元素都是唯一的, 且不考虑顺序, 所以想到使用 set

## 题解

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        for num in nums1:
            if (num in nums2 and num not in result):
                result.add(num)
        return result
```
