class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            z=i+1
            if z<len(nums):
                while nums[z]<nums[z-1] and z>=1:
                    print(f'z:{z}')
                    temp=nums[z-1]
                    nums[z-1]=nums[z]
                    nums[z]=temp
                    z-=1