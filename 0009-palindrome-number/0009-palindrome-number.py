class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = x

        # a negative number cant have palinfdrome 
        if(x<0):
            return False
        else:
            reverse = 0 
            while(a>0):
                num = a%10 
                reverse = (reverse*10) + num 
                a = a//10 
        if( reverse == x ):
            return True 
        else:
            return False 

