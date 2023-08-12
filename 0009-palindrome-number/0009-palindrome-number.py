class Solution:
    def isPalindrome(self, x: int) -> bool:

        # a negative number cant have palinfdrome 
        if(x<0):
            return False
        else:
            reverse = 0 
            digit = 0 
            while(x // 10**digit): 
                reverse = (reverse*10) + (x// (10**digit)%10)
                digit +=1
        if( reverse == x ):
            return True 
        else:
            return False 

