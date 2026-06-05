"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        mpp = defaultdict(int)
        for i in intervals:
            mpp[i.start] += 1
            mpp[i.end] -= 1
        
        count = maxCount = 0
        for i in sorted(mpp.keys()):
            count += mpp[i]
            maxCount = max(count,maxCount)
        
        return maxCount