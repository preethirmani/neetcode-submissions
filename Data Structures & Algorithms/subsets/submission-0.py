class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def recursive_set(cur_index, cur_set):
            if cur_index == n:
                result.append(cur_set[:])
                return
            cur_set.append(nums[cur_index])
            recursive_set(cur_index+1, cur_set)
            cur_set.pop()
            recursive_set(cur_index+1, cur_set)
        recursive_set(0,[])
        return result

