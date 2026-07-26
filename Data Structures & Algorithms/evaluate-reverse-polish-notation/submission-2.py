class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t == "+":
                st.append(st.pop() + st.pop())
            elif t == "-":
                num1, num2 = st.pop(), st.pop()
                st.append(num2-num1)
            elif t == "*":
                st.append(st.pop()*st.pop())
            elif t == "/":
                num1, num2 = st.pop(), st.pop()
                st.append(int(float(num2) / num1))
            else:
                st.append(int(t))
        return st[0]
            
