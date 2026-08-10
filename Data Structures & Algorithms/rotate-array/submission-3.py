class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left, right):
            while left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                left += 1

        n = len(nums)
        k = k % n if k >= n else k
        reverse (0,n - 1 ) #[8,7,6,5,4,3,2,1]
        reverse(0,k - 1)
        reverse(k, n - 1)
        # [1,2,3,4,5,6,7,8] 
        # k = 0, same, k = 8 , then k = 0, k = 9 
        
            

           
        