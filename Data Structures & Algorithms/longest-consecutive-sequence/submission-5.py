class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0
        max_length=0
        group_list=[]
        nums_s=sorted(nums)
        group_list.append(nums_s[0])
        for i in range(0,len(nums_s)-1):
            if nums_s[i+1]-nums_s[i]<=1:
                group_list.append(nums_s[i+1])
            else:
                length=len(set(group_list))
                max_length=length if max_length<length else max_length
                group_list.clear()
                group_list.append(nums_s[i+1])
        length=len(set(group_list))
        max_length=length if max_length<length else max_length    
        return max_length
        