class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def recursive_permute(start):
            if start == n :
                result.append(nums.copy())
                return
            for i in range(start, n):
                nums[i], nums[start] = nums[start], nums[i]
                recursive_permute(start+1)
                nums[i], nums[start] = nums[start], nums[i]
        
        recursive_permute(0)
        return result
        

