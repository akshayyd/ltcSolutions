class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=0
        b=x if x>0 else -x
        
        while b:
            if a > 2 ** 31 // 10:
                return False
            
            else:
                a = a * 10 + b % 10
                b = b//10
            
        if a == x:
            return True
        else:
            return False