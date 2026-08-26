class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cursum, total):
            if total == target:
                res.append(cursum.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            cursum.append(nums[i])
            dfs(i,cursum,total+nums[i])
            cursum.pop()
            dfs(i+1,cursum,total)
        
        dfs(0,[],0)
        return res