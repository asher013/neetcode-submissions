class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        st = []
        left = [-1] * n
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
        
        st = []
        right = [n] * n
        for i in range(n-1,-1,-1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        
        maxArea = 0
        for i in range(n):
            left[i] += 1
            right[i] -= 1
            maxArea = max(maxArea, heights[i] * (right[i]-left[i] + 1))
        return maxArea

            
