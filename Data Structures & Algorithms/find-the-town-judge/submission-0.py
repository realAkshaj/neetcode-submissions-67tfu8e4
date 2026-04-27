class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        iTrust = defaultdict(int)
        trustedBy = defaultdict(int)
        
        for src,dst in trust:

            trustedBy[dst] += 1
            iTrust[src] += 1
        
        for i in range(1, n + 1):
            if iTrust[i] == 0 and trustedBy[i] == n - 1:
                return i
        
        return -1
