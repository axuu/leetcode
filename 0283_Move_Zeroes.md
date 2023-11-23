## 回顾与思考

思考到了双指针的方法, 但最开始没有想出来如何设置操作指针. 所以先用了一个较为暴力的方法来解: 从末尾开始遍历数组, 遇到 0 之后, 将当前位置之后的所有元素前移 1 位, 并将最后一位设置为 0. 但这种方法的时间复杂度是 O(n^2), 不理想.

参考答案的双指针解法: 设置两个指针 slow 和 fast, 进行单次遍历, fast 在每次循环时都会向后移动, slow 只有在不为 0 的时候才向后移动 (即 slow 会停留在 0 的位置上), 等待 fast 指向的值与他交换.

## 题解

```python
# 方法一
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = len(nums) - 1
        while i >= 0:
            if (nums[i] == 0):
                for j in range(i, len(nums) - 1):
                    nums[j] = nums[j + 1]
                nums[-1] = 0
            i -= 1

# 方法二
class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1
```
