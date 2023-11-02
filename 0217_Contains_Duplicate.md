## 思考

和 136, 169 类似, 也是数组计数问题, 之前使用 hash map 的做法, 这次使用 Python 内置的 set

## 题解

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if (num in seen):
                return True
            seen.add(num)
        return False
```
