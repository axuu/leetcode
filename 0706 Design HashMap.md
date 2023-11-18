## 回顾与思考

核心还是在初始化存储的数据结构和哈希函数的设计上, 依然用了 0705 中的 Multiplicative hashing

区别在于这次存储的是键值对, 于是设计了一个 Pair 类

## 题解

```python
# 方法一 简单的数组
class Pair:
    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val

class MyHashMap:

    def eval_hash(self, key):
        return ((key*1031237) & (1<<20) - 1)>>5

    def __init__(self):
        self.arr = [[] for _ in range(1<<15)]

    def put(self, key: int, value: int) -> None:
        t = self.eval_hash(key)
        the_node = None
        for p in self.arr[t]:
            if (p.key == key):
                the_node = p

        if (the_node == None):
            pair = Pair(key, value)
            self.arr[t].append(pair)
        else:
            the_node.val = value

    def get(self, key: int) -> int:
        t = self.eval_hash(key)
        the_node = None
        for p in self.arr[t]:
            if (p.key == key):
                the_node = p
        return the_node.val if the_node != None else -1

    def remove(self, key: int) -> None:
        t = self.eval_hash(key)
        the_node = None
        for p in self.arr[t]:
            if (p.key == key):
                the_node = p
        if (the_node != None):
            self.arr[t].remove(the_node)

```
