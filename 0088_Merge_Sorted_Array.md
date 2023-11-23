## 回顾与思考

需要一定的思维技巧, 没有想到使用双指针的方法.

1. 对于两个已排序的列表, 只比较两个列表的最大值就可以了.
2. 对于该题的题干, 适合从列表末尾开始遍历.
3. 边缘 case, 对于 nums1 有两个元素, nums2 只有一个元素, 且 nums2 的元素比 nums1 的第一个元素小. 如: nums1 = [2, 0], nums2 = [1]
4. 如果使用内置函数, 应该比较简单

## 题解

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
```
