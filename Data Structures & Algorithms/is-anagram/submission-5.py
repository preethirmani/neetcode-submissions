class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        str_map = {}
        for c in s:
            if c in str_map :
                str_map[c] = str_map[c] + 1
            else :
                str_map[c] = 1
        for ch in t:
            if ch not in str_map :
                return False
            else :
                if str_map[ch] <= 0 :
                    return False
                else :
                    str_map[ch] = str_map[ch] - 1
                
        
        return True
               


