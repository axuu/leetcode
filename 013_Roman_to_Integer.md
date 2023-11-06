## 思考

从左到右, 利用单个指针依次判断字符串, 判断特殊情况, 即两个字符的情况. 再判断单个字符.

## 题解

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        map1 = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        map2 = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        i = 0
        result = 0
        while i < len(s):
            if(i < len(s) - 1 and map2.get(s[i] + s[i+1])):
                result += map2[s[i] + s[i+1]]
                i += 2
            else:
                result += map1[s[i]]
                i += 1
        return result
```
