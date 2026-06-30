class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_map = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in result_map:
                result_map[sorted_str].append(str)
            else:
                result_map[sorted_str] = [str]
        
        return(list(result_map.values()))
        