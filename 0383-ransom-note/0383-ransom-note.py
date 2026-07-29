from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        st=Counter(magazine)
        for ch in ransomNote:
            if st[ch]==0:
                return False
            st[ch]-=1
        return True
        