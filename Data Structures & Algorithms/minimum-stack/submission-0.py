class MinStack:

    def __init__(self):
        self.min_stack = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()

    def top(self) -> int:
        n = len(self.min_stack)
        return self.min_stack[n - 1]

    def getMin(self) -> int:
        min = math.inf
        for num in self.min_stack:
            if num < min:
                min = num
        return min
        
