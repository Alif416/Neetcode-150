class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cur=1
        res=1
        nums.sort()
        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i-1]==nums[i]:
                continue
            if nums[i]==nums[i-1]+1:
                cur+=1
            else:
                cur=1
            res=max(res,cur)
        return res

            

        