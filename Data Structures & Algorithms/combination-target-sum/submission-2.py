class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i,cursum,total):
            if total == target:
                res.append(cursum.copy())
                return
            if total > target or i >= len(nums):
                return
            
            cursum.append(nums[i])
            backtrack(i,cursum,total+nums[i])
            cursum.pop()
            backtrack(i+1,cursum,total)
        
        backtrack(0,[],0)
        return res