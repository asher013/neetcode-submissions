class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        freq1, need = {}, len(t)
        for c in t:
            freq1[c] = freq1.get(c,0) + 1
        minstr, length = "", float('inf')
        for i in range(len(s)):
            freq2, cur = {}, 0
            for j in range(i, len(s)):
                freq2[s[j]] = freq2.get(s[j],0) + 1
                if freq1.get(s[j],0) == freq2[s[j]]:
                    cur += freq2[s[j]]
                if cur == need:
                    if j - i + 1 < length:
                        minstr,length = s[i:j+1], j-i+1
        return minstr
                
                