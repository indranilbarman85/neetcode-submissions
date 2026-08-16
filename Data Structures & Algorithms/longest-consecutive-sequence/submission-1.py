class Solution:

    def find(self,nums: List[int])->List[List[int]]:

        group_set=[]
        group_list=[]
        nums_s=sorted(nums)
        group_list.append(nums_s[0])
        for i in range(0,len(nums_s)-1):
            if nums_s[i+1]-nums_s[i]<=1:
                group_list.append(nums_s[i+1])
            else:
                group_set.append(group_list.copy())
                group_list.clear()
                group_list.append(nums_s[i+1])
        # group_list.append(nums_s[-1])
        group_set.append(group_list.copy())
            
        return group_set

            


    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_lenth=0
        if len(nums)==0:
            return 0
        lst=self.find(nums)
        for l in lst:
            if max_lenth<len(set(l)):
                max_lenth=len(set(l))
        return max_lenth
        