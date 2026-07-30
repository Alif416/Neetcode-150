class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ''.join(map(str, digits))
        final=int(res)+1
        new=str(final)
        rev=[]
        for i in new:
            rev.append(int(i))
        return rev
        