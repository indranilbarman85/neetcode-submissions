class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        i=0
        j=len(people)-1
        
        count=0

        while i<=j:
            remain=limit-people[i]
            
            if remain==0 or remain<people[j]:
                count+=1
                i+=1
            elif remain>=people[j]:
                count+=1
                i+=1
                j-=1
            else:
                i+=1
            
        return count