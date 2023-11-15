## 回顾与思考

设计一个 HashSet, 支持 add、remove 和 contains 操作, 此题的实现方法有很多，可以使用数组、链表等等. 因为题目给了范围限制:

Constraints:

- 0 <= key <= 1000000
- At most 10000 calls will be made to add, remove, and contains.

所以怎样实现都可以. 但我认为还是需要了解真正的哈希函数的方法.

在一个题解中见到 Multiplicative hashing: 详解(链接)[https://leetcode.com/problems/design-hashset/solutions/768659/python-easy-multiplicative-hash-explained/]

## 题解

```python
# 方法一 简单的数组
class MyHashSet:
    def __init__(self):
        self.buckets = [None] * 100000

    def hash_func(self, key: int) -> int:
        index = key % 100000
        return index

    def add(self, key: int) -> None:
        index = self.hash_func(key)
        self.buckets[index] = key

    def remove(self, key: int) -> None:
        index = self.hash_func(key)
        self.buckets[index] = None

    def contains(self, key: int) -> bool:
        return key in self.buckets

# 方法二
class MyHashSet:
    def eval_hash(self, key):
        return ((key*1031237) & (1<<20) - 1)>>5

    def __init__(self):
        self.arr = [[] for _ in range(1<<15)]

    def add(self, key: int) -> None:
        t = self.eval_hash(key)
        if key not in self.arr[t]:
            self.arr[t].append(key)

    def remove(self, key: int) -> None:
        t = self.eval_hash(key)
        if key in self.arr[t]:
            self.arr[t].remove(key)

    def contains(self, key: int) -> bool:
        t = self.eval_hash(key)
        return key in self.arr[t]

```
