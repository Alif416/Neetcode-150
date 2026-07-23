class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        hashmap={}
        for i in range(len(strs)):
            s=strs[i]
            s=''.join(sorted(s))
            if s not in hashmap:
                hashmap[s]=len(res)
                res.append([])
            res[hashmap[s]].append(strs[i])
        return res        