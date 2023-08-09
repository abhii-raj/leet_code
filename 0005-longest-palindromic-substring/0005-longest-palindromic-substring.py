class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_pa(s):
            return(s == s[::-1])
        #Grow from center
        biggest = s[0]
        step = len(biggest)//2

        #handle single letter centers
        for center in range(1, len(s)-1):
            bounds = [center-(1+step), center+(1+step)]
            while (bounds[0] > -1 ) and (bounds[1]< len(s)):
                if check_pa(s[bounds[0]:bounds[1]+1]):
                    biggest = s[bounds[0]:bounds[1]+1]
                    step = len(biggest)//2
                    bounds[0] -=1
                    bounds[1] +=1
                else:
                    break

        # Handle double letter centers
        for center in range(0,len(s)-1):
            bounds = [center-(step), center+(1+step)] #extend it upto lenght 2
            while (bounds[0] > -1 ) and (bounds[1]< len(s)):
                if check_pa(s[bounds[0]:bounds[1]+1]):
                    biggest = s[bounds[0]:bounds[1]+1]
                    step = len(biggest)//2
                    bounds[0] -=1
                    bounds[1] +=1
                else:
                    break
            
        return biggest


            


