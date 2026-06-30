class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}
        result = []
        for i, num in enumerate(nums) :
            nums_map[num] = nums_map[num] + 1 if num in nums_map else 1

        sorted_list = sorted(nums_map.items(), key = lambda item : item[1], reverse = True)

        for i in range(k) :
            result.append(sorted_list[i][0])

        
        return result

            