class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i,cursum,total):
            if total == target:
                res.append(cursum.copy())
                return
            if i >= len(candidates) or total > target:
                return
            cursum.append(candidates[i])
            dfs(i+1,cursum,total+candidates[i])
            cursum.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1,cursum,total)
        
        dfs(0,[],0)
        return res
