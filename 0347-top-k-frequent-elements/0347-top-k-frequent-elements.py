from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=Counter(nums)
        pq=[]
        result=[]
        for key,freq in hashmap.items():
            heapq.heappush(pq,[freq,key])
            if len(pq)>k:
                heapq.heappop(pq)
        temp=[0]*len(pq)
        idx=len(pq)-1
        while pq:
            temp[idx]=heapq.heappop(pq)[1]
            idx-=1
        for i in temp:
            result.append(i)
        return result
