## 思考

需要一定的思维技巧, 没有想到使用双指针的方法.

1.

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
