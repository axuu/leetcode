## 回顾与思考

寻找两个数组的交集, 和 349 不同的是, 要求结果中尽可能多地出现两个数组中的元素.

自己的思路是, 用两个 map 分别计算两个数组中元素出现的次数, 然后再次遍历, 寻找共有元素, 并且次数取较小值, 最后生成新的数组返回结果.

参考别人的答案, 使用了 defaultdict 进行简化.

defaultdict 是 Python 内置的一个字典子类，它提供了一个默认值的概念，即在字典中访问不存在的键时，如果该键没有任何值，它会使用默认工厂函数指定的默认值。这可以防止 "KeyError" 异常的发生。

你必须使用 collections 模块来导入 defaultdict。在创建一个 defaultdict 对象时，你需要指定工厂函数，以指定默认值的类型。工厂函数可以是内置的 Python 类型（如 int，float，str），也可以是自定义函数。

下面是一个使用 defaultdict 的例子，并将默认值设置为 0

```python
from collections import defaultdict
# 使用 int 作为默认工厂函数
my_dict = defaultdict(int)
```

方法二的巧妙之处在于, 遍历 nums2 时, 如果符合要求, 将元素添加到结果并将 map 中的计数减 1, 这样当计数为 0 时, 说明该元素在 nums1 中出现的次数已经用完, 不需要再添加到结果中了.

## 题解

```python
# 方法一
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = {}
        map2 = {}

        for num in nums1:
            if (num in map1):
                map1[num] += 1
            else:
                map1[num] = 1

        for num in nums2:
            if (num in map2):
                map2[num] += 1
            else:
                map2[num] = 1

        result = []
        for num in map1.keys():
            if (num in nums2):
                count = map2[num] if map1[num] > map2[num] else map1[num]
                result += [num] * count

        return result

# 方法二
from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = defaultdict(int)
        for i in nums1:
            s[i] +=1
        ans = []
        for i in nums2:
            if s[i]>0:
                ans.append(i)
                s[i] -=1

        return ans
```
