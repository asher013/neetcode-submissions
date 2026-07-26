class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        parenths = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in parenths:
                if st and st[-1] == parenths[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        
        return True if not st else False
            

