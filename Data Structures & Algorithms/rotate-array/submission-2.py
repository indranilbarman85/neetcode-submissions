class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n

        def reverse(lw,hi):
            while lw<hi:
                nums[lw],nums[hi]=nums[hi],nums[lw]
                lw+=1
                hi-=1
                
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)