class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_frequency = 0
        max_length = 0
        count = {}
        for right in range(len(s)):
            cur_ch = s[right]
            count[cur_ch]=count.get(cur_ch, 0)+1
            max_frequency = max(max_frequency, count.get(cur_ch))
            while (right-left)+1 - max_frequency > k:
                temp = s[left]
                count[temp] = count.get(temp)-1
                left += 1
            max_length = max(max_length, (right-left)+ 1)
        return max_length