class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       r, l = 1, 1
       result = [1] * len(nums)
       n = len(nums)
       for i in range(n):
        result[i] = result[i] * l
        l = l * nums[i]
       for i in range(n-1, -1, -1):
        result[i] = result[i] * r
        r = r * nums[i]
       return result
    
    
        
        
 
        
            
        