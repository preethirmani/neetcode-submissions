class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            if self.min_stack[-1] >= val:
                self.min_stack.append(val)
        self.stack.append(val)


    def pop(self) -> None:
        min_len = len(self.min_stack)
        stack_len = len(self.stack)
        if self.min_stack and self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()


    def top(self) -> int:
        n = len(self.stack)
        return self.stack[n - 1]

    def getMin(self) -> int:
       return self.min_stack[-1]
        
