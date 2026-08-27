class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i,cursum,total):
            if total == target:
                res.append(cursum.copy())
                return
            if total > target or i >= len(candidates):
                return
            cursum.append(candidates[i])
            backtrack(i+1,cursum,total+candidates[i])
            cursum.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1,cursum,total)
        
        backtrack(0,[],0)
        return res

