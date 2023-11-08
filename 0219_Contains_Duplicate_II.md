## 思考

nums[i] == nums[j] 意味着相等的数字出现至少两次, 且满足附加条件: abs(i - j) <= k

使用 hash map 可以避免 i == j 的情况, 用 map[nums[i]] = i 记录每个数字位置

需要注意的是同一个数字可能会出现超过两次, 在比对 abs(i - j) <= k 不成功后, 需要记录每个数字最后一次出现的位置

## 题解

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for i in range(len(nums)):
            if (nums[i] in map and abs(i - map[nums[i]]) <= k):
                return True
            else:
                map[nums[i]] = i
        return False
```
