class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        meh = 0
        msf = -math.inf
        for num in nums:
            meh = meh + num
            if meh < num:
                meh = num
            if msf < meh:
                msf = meh
        return msf
