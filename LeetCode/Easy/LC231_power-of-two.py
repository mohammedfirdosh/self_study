class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # https://leetcode.com/problems/power-of-two
        #print(f"Value of n: {n}")
        if n <= 0:
            #print("cond-1")
            return False
        elif n in [1,2]:
            #print("cond-2")
            return True
        elif n > 2:
            #print("cond-3")
            if n %  2 != 0:
                #print("cond-3.1")                
                return False
            else:
                #print("cond-4")
                return self.isPowerOfTwo(n//2)
        
