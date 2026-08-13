class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       stack = []
       operator = ['+', '-', '*', '/']
       for token in tokens:
            print(token)
            if token not in operator:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    stack.append(right+left)
                elif token == '*':
                    stack.append(left*right)
                elif token == '-':
                    diff = left - right 
                    stack.append(diff)
                else:
                    quotient = int(left / right)
                    stack.append(quotient)

       return stack.pop()
       
