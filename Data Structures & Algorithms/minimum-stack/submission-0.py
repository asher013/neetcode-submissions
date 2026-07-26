class MinStack:

    def __init__(self):
        self.st = []
        self.prest = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if self.prest:
            val = min(val,self.prest[-1])
        self.prest.append(val)

    def pop(self) -> None:
        self.st.pop()
        self.prest.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.prest[-1]

        
