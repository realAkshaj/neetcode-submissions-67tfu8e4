class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)
        
        while len(stones) > 1:
            firstStone = heapq.heappop(stones)
            secondStone = heapq.heappop(stones)
            if secondStone > firstStone:
                heapq.heappush(stones,firstStone - secondStone)
            
        stones.append(0)

        return abs(stones[0])