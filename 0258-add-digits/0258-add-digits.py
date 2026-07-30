class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            total=0
            while num:
                digit=num%10
                total+=digit
                num=num//10
            num=total
        return num
            


        