class Solution:
    def isPalindrome(self, x: int) -> bool:

        # a negative number cant have palinfdrome 
        if(x<0):
            return False
        
        reverse = 0 
        digit = 0 
        while(x // 10**digit != 0): 
            reverse = (reverse*10) + (x// (10**digit)%10)
            digit +=1
        return ( reverse == x )
        

