class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini= float('inf')
        for i in nums:
            if i<mini:
                mini=i
        return mini
        