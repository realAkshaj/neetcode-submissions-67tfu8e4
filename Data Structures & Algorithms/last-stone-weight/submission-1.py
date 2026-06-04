class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)
        
        while len(stones) > 1:
            firstStone = abs(heapq.heappop(stones))
            secondStone = abs(heapq.heappop(stones))
            if firstStone > secondStone:
                heapq.heappush(stones,(firstStone - secondStone)*-1)
            
        stones.append(0)

        return abs(stones[0])