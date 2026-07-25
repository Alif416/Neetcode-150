class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set()
        res=0
        for val in nums:
            hashset.add(val)
        for val in hashset:
            if val in hashset and (val-1) not in hashset:
                curr=val
                count=0
                while curr in hashset:
                    curr+=1
                    count+=1
                res=max(count,res)
        return res 