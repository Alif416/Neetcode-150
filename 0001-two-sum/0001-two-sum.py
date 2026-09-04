class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(0,len(nums)):
            temp=target-nums[i]
            if temp in hashmap:
                return [hashmap[temp],i]
            hashmap[nums[i]]=i
        

    
        