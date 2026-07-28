class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mydict={}
        longest=0
        left=0
        right=0
        while right<len(s):
            if s[right] in mydict:
                left=max(left,mydict[s[right]]+1)
            mydict[s[right]]=right
            longest=max(longest,right-left+1)
            right+=1
        return longest

            
        