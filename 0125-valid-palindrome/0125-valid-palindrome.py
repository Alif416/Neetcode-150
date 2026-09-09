class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered=[]
        for i in s:
            if i.isalnum():
                filtered.append(i.lower())
        new_s=''.join(filtered)
        left=0
        right=len(filtered)-1
        while left<right:
            if new_s[left]!=new_s[right]:
                return False
            left+=1
            right-=1
        return True