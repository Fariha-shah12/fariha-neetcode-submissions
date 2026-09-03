class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        right, left = 0,0
        res = 0
        while right < len(s):
            index = ord(s[right]) - ord('A')
            count[index] +=1
            window_size = right - left +1
            if (window_size - max(count) <= k):
                res = max(window_size, res)
                right+=1
            else:
                index= ord(s[left]) - ord('A')
                count[index] -=1
                left +=1
                right+=1
        return res