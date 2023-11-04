class Solution:
    def majorityElement(nums: list[int]) -> int:
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
            print('candidate', candidate)
            print('count', count)
            print('----------')
        
        return candidate
    
Solution.majorityElement([2,2,1,1,1,1,1,2,3])