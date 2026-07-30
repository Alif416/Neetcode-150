class Solution:
    def reverse(self, x: int) -> int:
        int_max=2**31-1
        int_min=-2**31

        sign=-1 if x<0 else 1
        rev=0
        x=abs(x)
        while x:
            digit=x%10
            x=x//10
            rev=rev*10+digit
        res=rev*sign
        if res>int_max or res<int_min:
            return 0
        return res


        