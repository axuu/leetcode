## 回顾与思考

本题有几个难点, 一个是利用自带函数 sorted 对字符串数组进行排序, 然后比较最长的字符串和最短的字符串即可.

第二个是边缘情况比较难处理, 比如[""], ["", ""] 等情况, 如果用切片的方式如 str[:i] 来处理, 会出现部分 case 不能通过的情况.

## 题解

```python
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        result = ''
        for i in range(len(strs[0])):
            if (first[i] != last[i]):
                break
            result += first[i]
        return result
```
