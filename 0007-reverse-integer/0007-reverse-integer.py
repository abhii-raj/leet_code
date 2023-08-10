class Solution:
    def reverse(self, x: int) -> int:
        if(x>0):
            reverse =0
            while x !=0:
                digit= x%10
                reverse = reverse*10 + digit
                x = x//10
            if(reverse<2147483648):
                return reverse
            else:
                return 0
            
            

        else:
            x= -x
            reverse =0
            while x!=0:
                digit = x%10
                reverse = reverse*10 + digit
                x = x//10
            if(reverse<2147483648):
                reverse = -reverse
                return reverse
            else:
                return 0


        

