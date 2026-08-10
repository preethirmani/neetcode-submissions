class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1 : return False
        ch_map = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }
        stack = []
        for c in s:
            if c not in ch_map:
                stack.append(c)
            else:
                if len(stack) == 0 : return False
                temp = stack.pop()
                if temp != ch_map.get(c):
                    return False
        return len(stack) == 0
