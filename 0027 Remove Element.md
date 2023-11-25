## 回顾与思考

考虑使用双指针的方法, 即当前指针和尾指针两个指针, 当前指针指向的元素被替换后, 需要将尾指针指向的元素替换到当前指针指向的位置, 并将尾指针指向的元素置为"\_"(或者其他不会出现在数组中的值), 并将尾指针向前移动一位.

比较难处理的是指针的位数问题, 导致 [] 等边缘 case 出现错误.

## 题解

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                nums[j] = "_"
                j = j - 1
            else:
                i = i + 1
        return j + 1
```
