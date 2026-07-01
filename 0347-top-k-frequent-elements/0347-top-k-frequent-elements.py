from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=Counter(nums)
        min_heap=[]
        for key,freq in hashmap.items():
            heapq.heappush(min_heap,(freq,key))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return [key for freq,key in min_heap]

        


        