class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        boats = left = 0
        right = len(people) - 1
        res = 0

        while left <= right:

            leftover = limit - people[right]
            right -= 1
            res += 1

            if left <= right and leftover >= people[left]:
                left += 1
        return res