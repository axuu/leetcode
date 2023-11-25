## 回顾与思考

在数组上定义两个指针 i 和 j,

## 题解

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            if (map.get(num)):
                map[num] += 1
            else:
                map[num] = 1
        for key in map:
            if (map[key]) == 1:
                return key
```
