class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst=[]

        for num in range(len(nums)):
            target=nums[num]
            i=0
            j=len(nums)-1
            while i<j and i!=num and j!=num:
                if nums[i]+nums[j]>-target:
                    j-=1
                elif nums[i]+nums[j]<-target:
                    i+=1
                else:
                    entry=[nums[i],target,nums[j]]
                    entry.sort()
                    if entry not in lst:
                        lst.append(entry)
                    i+=1
        return lst