class Solution:
    def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:  
        if (m == 0 or n == 0):
            return
        for target in nums2:
            print(target)
            for i in range(m + n - 1, -1, -1):
                if (target > nums1[i] and nums1[i+1] == 0):
                    nums1[i+1] = target
                    break
                if (target >= nums1[i-1] and target < nums1[i]):
                    nums1[i] = target
                    break
                else:
                    nums1[i] = nums1[i - 1]
                print(nums1)

        return nums1
    
print(Solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
