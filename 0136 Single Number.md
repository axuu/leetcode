## 回顾与思考

实质上是对一个数组中出现的元素进行计数的问题, 然后找到计数为 1 的元素. 使用的是哈希表.

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
