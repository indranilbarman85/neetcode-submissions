class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import defaultdict
        countColor=defaultdict(int)

        countColor[0]=0
        countColor[1]=0
        countColor[2]=0

        for i in range(len(nums)):
            countColor[nums[i]]+=1

        i=0

        for item in countColor.items():
            for z in range(item[1]):
                nums[i]=item[0]
                i+=1
        