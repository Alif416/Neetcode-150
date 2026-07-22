from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_new=''.join(sorted(s))
        t_new=''.join(sorted(t))
        if s_new==t_new:
            return True
        else:
            return False
        

      



         