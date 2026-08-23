class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dictNo={}

        for i in range(len(nums)):
            val=dictNo.get(nums[i],-1)
            if val!=-1:
                if (i-val) <= k:
                    return True
            dictNo[nums[i]]=i
        return False