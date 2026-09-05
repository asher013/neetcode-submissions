class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # what are the possible next states? Either partition on current character, or bring in next character
        res, part = [], [] # final list of states, current list of states
        def isPali(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l,r = l+1,r-1
            return True
        def dfs(j,i):
            if i >= len(s): # goal predicate
                if i == j:
                    res.append(part.copy())
                return
            
            if isPali(j,i): # check if state is acceptable
                part.append(s[j:i+1]) # add to accepted states
                dfs(i+1,i+1) # choose next possible state (partition on character)
                part.pop() # backtrack
            
            dfs(j,i+1) # choose next possible state (merge next character)
        
        dfs(0,0)
        return res