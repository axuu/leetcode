## 思考

方法一: 把数组排序后, 中间的元素一定是数量大于 n/2 的元素. 注意 Python 的整除是 `//`.

方法二: 类似于 0136_Single_Number, 使用哈希表记录每个元素出现的次数, 最后返回出现次数最多的元素.

方法三: 摩尔投票法（Boyer–Moore majority vote algorithm）, 是一个很巧妙的算法也被称作「多数投票法」, 算法解决的问题是：如何在任意多的候选人中（选票无序）, 选出获得票数最多的那个.

1. 假定一个候选人, 其他候选人和假定候选人的票数进行两两对抗抵消
2. 如果抵消票数到 0, 更换候选人

## 题解

```python
# 方法一
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]

# 方法二
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

# 方法三
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
```
