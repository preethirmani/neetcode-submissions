class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in result_map:
                return [result_map[diff], i]
            else:
                result_map[num] = i
        
                
