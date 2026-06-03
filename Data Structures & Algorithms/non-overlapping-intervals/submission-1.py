class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        
        res = []
        intervals.sort(key=lambda x: x[1])

        for start,end in intervals:

            if not res or res[-1][1] <= start:
                
                res.append([start,end])
            
        diff = len(intervals) - len(res)
        return diff
