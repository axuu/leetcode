## 回顾与思考

找到数组的中点索引: `mid = len(nums) // 2`, 所有数组都可以用这个方法寻找中间元素.

递归的返回值可以直接返回树的节点, 在递归的步骤里, 每次都把数组拆分成左右两半, 创建根节点, 传递下去.

边缘 case: 如果数组为空, 返回 None

## 题解

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        total_nums = len(nums)

        if (total_nums == 0):
            return None

        mid = total_nums // 2
        return TreeNode(
            nums[mid],
            self.sortedArrayToBST(nums[:mid]),
            self.sortedArrayToBST(nums[mid+1:])
        )

```
