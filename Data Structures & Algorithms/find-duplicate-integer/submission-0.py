class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_map = {}
        for num in nums:
            if num in num_map:
                return num
            else:
                num_map[num] = 1

        return None