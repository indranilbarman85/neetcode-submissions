class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        ori=len(nums)
        for i in range(len(nums)):
            if nums[i]==val:
                k+=1

        for i in range(k):
            nums.remove(val)
        return ori-k
        