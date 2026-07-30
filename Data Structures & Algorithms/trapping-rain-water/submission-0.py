class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = 0,0
        water = 0
        n = len(height)
        left_max_arr = [0] * n
        right_max_arr = [0] * n
        min_height = 0

        for i in range(n):
            j = -i-1
            left_max_arr[i] = left_max
            left_max = max(left_max, height[i])
            right_max_arr[j] = right_max
            right_max = max(right_max, height[j])

        for i in range(n):
            min_height = min(left_max_arr[i], right_max_arr[i])
            water += max(min_height - height[i], 0)

        return water
