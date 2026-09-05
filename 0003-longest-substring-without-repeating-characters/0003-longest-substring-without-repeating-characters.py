class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left, right = 0, 0
        vis = set()
        res = 0

        while right < n:
            while s[right] in vis:
                vis.remove(s[left])
                left += 1

            vis.add(s[right])
            res = max(res, right - left + 1)
            right += 1

        return res