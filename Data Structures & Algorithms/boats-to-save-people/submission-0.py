class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people) - 1
        count = 0
        people.sort()
        while l <= r:
            remain = limit - people[r]            
            r = r - 1            
            count = count + 1
            if l <= r and remain >=  people[l]:
                l  = l + 1
            

        return count
