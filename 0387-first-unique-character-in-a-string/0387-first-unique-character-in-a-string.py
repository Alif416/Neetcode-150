from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        st=Counter(s)
        my_dict={}
        for i in range(len(s)):
            my_dict[s[i]]=i
        for key,val in st.items():
            if st[key]==1:
                return my_dict[key]
        return -1