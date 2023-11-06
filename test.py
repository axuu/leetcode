class Solution:
    def removeElement(nums: list[int], val: int) -> int:
        if(len(nums) == 1):
            if(nums[0] == val):
                return 0
            else:
                return 1

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

    
print(Solution.removeElement([3,3], 3))